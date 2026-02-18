# External Integrations

**Analysis Date:** 2026-02-18

## APIs & External Services

**None**
- This is a utility library with no external API integrations or third-party service calls.

## Data Storage

**Databases:**
- None - This is a stateless utility library that does not interact with databases.

**File Storage:**
- Local filesystem only - Library processes in-memory JSON objects passed as Python data structures. No file I/O operations.

**Caching:**
- None - No caching layer implemented.

## Authentication & Identity

**Auth Provider:**
- None - No authentication or authorization mechanisms required. Public library with no access control.

## Monitoring & Observability

**Error Tracking:**
- None - Library raises `JsonParserException` for validation errors (`src/json_parser/__init__.py`). Error tracking must be implemented by consuming application.

**Logs:**
- None - No logging implemented. Library uses no logging framework.

## CI/CD & Deployment

**Hosting:**
- PyPI (Python Package Index) - Package distributed via `pip install json-key-parser`
- Source: GitHub repository at `https://github.com/diverdale/json_parser`

**CI Pipeline:**
- None detected - No `.github/workflows/` or CI configuration files present.

## Environment Configuration

**Required env vars:**
- None - Library requires no environment variables.

**Secrets location:**
- Not applicable - No secrets or credentials required.

## Webhooks & Callbacks

**Incoming:**
- None - Library does not expose any endpoints or webhooks.

**Outgoing:**
- None - Library does not make external requests or call webhooks.

## PyPI Configuration

**Package Details:**
- Name: `json-key-parser`
- Version: 0.0.2 (from `pyproject.toml`)
- License: MIT
- Homepage: `https://github.com/diverdale/json_parser`
- Repository: `https://github.com/diverdale/json_parser`

---

*Integration audit: 2026-02-18*
