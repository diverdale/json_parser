import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "json_parser",
    version = "0.0.1",
    author = "Dale Wright",
    author_email = "diverdale@gmail.com",
    description = "Dynamic JSON parser",
    long_description = long_description,
    url = "https://github.com/diverdale/json_parser",
    classifiers = [
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where="src"),
    python_requires = ">=3.6"
)