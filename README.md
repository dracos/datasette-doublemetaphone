# datasette-doublemetaphone

[![PyPI](https://img.shields.io/pypi/v/datasette-doublemetaphone.svg)](https://pypi.org/project/datasette-doublemetaphone/)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/dracos/datasette-doublemetaphone/blob/master/LICENSE)

Datasette plugin that adds custom SQL functions for fuzzy string matching,
built on top of the [Double Metaphone](https://github.com/dedupeio/doublemetaphone)
Python library.

As SQLite custom functions must return a string, we have separate calls for
the two results, or one that returns a JSON array of the two results.

Examples:

    SELECT double_metaphone_main("richard");
        -- Outputs 'RXRT'
    SELECT double_metaphone_alt("richard");
        -- Outputs 'RKRT'
    SELECT double_metaphone_json("richard");
        -- Outputs '["RXRT", "RKRT"]'
