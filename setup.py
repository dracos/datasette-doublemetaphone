from setuptools import setup
import os

VERSION = "0.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="datasette-doublemetaphone",
    description="Datasette plugin adding SQL functions for Double Metaphone fuzzy text matching",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Matthew Somerville",
    url="https://github.com/dracos/datasette-doublemetaphone",
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["datasette_doublemetaphone"],
    entry_points={"datasette": ["doublemetaphone = datasette_doublemetaphone"]},
    install_requires=["datasette", "doublemetaphone"],
)
