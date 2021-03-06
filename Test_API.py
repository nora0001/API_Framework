import pytest
from poetry import poetry


def test_t01():
    value={'Date': 'Sat, 06 Mar 2021 06:29:29 GMT', 'Content-Type': 'application/json', 'Content-Length': '390',
           'Server': 'gunicorn/19.9.0', 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Credentials': 'true',
           'Connection': 'keep-alive'}
    a=value["Server"]
    print(a)