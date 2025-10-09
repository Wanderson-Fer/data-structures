# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=redefined-outer-name

import pytest
from src.hash_table import HashTable

@pytest.fixture
def ht():
    return HashTable(10)

def test_add_and_get(ht):
    ht["apple"] = 5
    assert ht["apple"] == 5

def test_overwrite_value(ht):
    ht["banana"] = 10
    ht["banana"] = 20
    assert ht["banana"] == 20

def test_get_nonexistent_key(ht):
    assert ht["notfound"] is None

def test_collision(ht):
    # Force collision by using keys with same hash
    key1 = "a"
    key2 = chr(ord("a") + ht.max)
    ht[key1] = "first"
    ht[key2] = "second"
    # Only the last value will be stored due to collision (no chaining)
    assert ht[key1] == "second"
    assert ht[key2] == "second"
