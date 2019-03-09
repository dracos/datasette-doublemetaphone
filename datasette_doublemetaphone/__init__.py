import json
from datasette import hookimpl
from doublemetaphone import doublemetaphone

def _convert_dm_to_json(s):
    return json.dumps(doublemetaphone(s))

def _dm_result_main(s):
    return doublemetaphone(s)[0]

def _dm_result_alt(s):
    return doublemetaphone(s)[1]

@hookimpl
def prepare_connection(conn):
    conn.create_function('doublemetaphone_json', 1, _convert_dm_to_json)
    conn.create_function('doublemetaphone_main', 1, _dm_result_main)
    conn.create_function('doublemetaphone_alt', 1, _dm_result_alt)
