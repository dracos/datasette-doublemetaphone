from datasette_doublemetaphone import prepare_connection
import sqlite3
import pytest


@pytest.mark.parametrize(
    "sql,expected",
    (
        ('doublemetaphone_main("richard")', 'RXRT'),
        ('doublemetaphone_alt("richard")', 'RKRT'),
        ('doublemetaphone_json("richard")', '["RXRT", "RKRT"]'),
    ),
)
def test_doublemetaphone(sql, expected):
    conn = sqlite3.connect(":memory:")
    prepare_connection(conn)
    result = conn.execute("select " + sql).fetchone()[0]
    assert expected == result
