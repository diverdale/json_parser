# Dale Wright

# Parse JSON objects by key name
import fnmatch
import json
from typing import Union, List, Any, Optional


class JsonParserException(Exception):
    def __init__(self, msg: str):
        super().__init__(msg)


class JsonParser:
    """
        The JsonParser class.

        Methods:

        __init__(self, obj, args)
            returns the JsonParser object

        get_args(self):
            returns the arguments

        get_json(self):
            returns the JSON object

        get_data(self, path=False, max_depth=None):
            returns the parsed JSON data
    """

    def __init__(self, obj: Union[str, dict, list], args: List[str]):

        # API-01: If obj is a raw JSON string, parse it first
        if isinstance(obj, str):
            try:
                obj = json.loads(obj)
            except json.JSONDecodeError as e:
                raise JsonParserException(
                    msg=f"Invalid JSON string: {e}"
                )

        # API-02: If obj is a single dict (after possible string parsing), wrap it in a list
        if isinstance(obj, dict):
            obj = [obj]

        if not obj:
            raise JsonParserException(
                msg='JSON object must be present'
            )
        if not args:
            raise JsonParserException(
                msg='No keys present to parse'
            )

        self.json_obj = obj
        self.args = args

    def get_args(self):
        return(self.args)

    def get_json(self):
        return(self.json_obj)

    def _search_dict(
        self,
        dct: dict,
        keys_to_search: List[str],
        current_path: str = "",
        current_depth: int = 1,
        max_depth: Optional[int] = None,
        path: bool = False,
        case_sensitive: bool = True,
    ) -> dict:
        """Recursively search dct for matching keys.

        Args:
            dct: The dict to search.
            keys_to_search: List of key patterns (fnmatch-compatible).
            current_path: Dot-notation path accumulated so far.
            current_depth: Current recursion depth (1 = top level of input dict).
            max_depth: Maximum depth to search. None means unlimited.
            path: If True, wrap matched values as {"value": ..., "path": "..."}.
            case_sensitive: If False, key matching is case-insensitive (both sides lowercased
                            for comparison; output key always uses original JSON casing).

        Returns:
            Dict of matched keys to their values (or path-wrapped values).
        """
        # max_depth=0 means no recursion at all — return immediately
        if max_depth is not None and max_depth == 0:
            return {}

        found = {}

        def _merge(found: dict, key: str, value: Any) -> None:
            """Merge a new value for key into found, building lists on duplicates."""
            if key not in found:
                found[key] = value
            else:
                if not isinstance(found[key], list):
                    found[key] = [found[key]]
                if isinstance(value, list):
                    found[key].extend(value)
                else:
                    found[key].append(value)

        for key, value in dct.items():
            full_path = f"{current_path}.{key}" if current_path else key

            # Check if this key matches any search pattern
            for pattern in keys_to_search:
                if case_sensitive:
                    matched = fnmatch.fnmatch(key, pattern)
                else:
                    matched = fnmatch.fnmatch(key.lower(), pattern.lower())
                if matched:
                    matched_value = {"value": value, "path": full_path} if path else value
                    _merge(found, key, matched_value)
                    break  # a key only needs to match once per pattern set (also prevents case-variant query key duplication)

            # Recurse into nested dict (depth increases)
            if isinstance(value, dict):
                if max_depth is None or current_depth < max_depth:
                    nested_found = self._search_dict(
                        value,
                        keys_to_search,
                        current_path=full_path,
                        current_depth=current_depth + 1,
                        max_depth=max_depth,
                        path=path,
                        case_sensitive=case_sensitive,
                    )
                    for nested_key, nested_value in nested_found.items():
                        _merge(found, nested_key, nested_value)

            # Recurse into list items (lists are transparent — depth does NOT increase)
            elif isinstance(value, list):
                if max_depth is None or current_depth < max_depth:
                    for item in value:
                        if isinstance(item, dict):
                            nested_found = self._search_dict(
                                item,
                                keys_to_search,
                                current_path=full_path,
                                current_depth=current_depth,
                                max_depth=max_depth,
                                path=path,
                                case_sensitive=case_sensitive,
                            )
                            for nested_key, nested_value in nested_found.items():
                                _merge(found, nested_key, nested_value)

        return found

    def get_data(self, path: bool = False, max_depth: Optional[int] = None, case_sensitive: bool = True) -> List[Any]:
        """Return extracted keys from the JSON object.

        Args:
            path: If True, each matched value is wrapped as {"value": ..., "path": "dot.notation.path"}.
                  Default False preserves original bare-value behavior.
            max_depth: Maximum nesting depth to search. None (default) searches all levels.
                       1 = top-level keys only, 2 = one level of nesting, etc.
                       0 = return empty dict for every input item.
            case_sensitive: If False, key matching ignores capitalization (both key and pattern are
                            lowercased for comparison; output keys always use original JSON casing).
                            Default True preserves exact-match behavior for all existing callers.

        Returns:
            List with one dict per input item, containing matched keys and their values.
        """
        result = []
        for item in self.json_obj:
            if isinstance(item, dict):
                result.append(
                    self._search_dict(
                        item,
                        self.args,
                        current_path="",
                        current_depth=1,
                        max_depth=max_depth,
                        path=path,
                        case_sensitive=case_sensitive,
                    )
                )
        return result


def parse(obj: Union[str, dict, list], keys: List[str], path: bool = False, max_depth: Optional[int] = None, case_sensitive: bool = True) -> List[Any]:
    """One-liner convenience function. Equivalent to JsonParser(obj, keys).get_data(path=path, max_depth=max_depth, case_sensitive=case_sensitive)."""
    return JsonParser(obj, keys).get_data(path=path, max_depth=max_depth, case_sensitive=case_sensitive)
