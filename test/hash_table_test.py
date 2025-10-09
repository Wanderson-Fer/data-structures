# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=redefined-outer-name

import pytest
from src.hash_table import HashTable

@pytest.fixture
def ht():
    return HashTable(10)

def test_add_and_get(ht):
    ht.add("apple", 5)
    assert ht.get("apple") == 5

def test_overwrite_value(ht):
    ht.add("banana", 10)
    ht.add("banana", 20)
    assert ht.get("banana") == 20

def test_get_nonexistent_key(ht):
    assert ht.get("notfound") is None

def test_collision(ht):
    # Force collision by using keys with same hash
    key1 = "a"
    key2 = chr(ord("a") + ht.max)
    ht.add(key1, "first")
    ht.add(key2, "second")
    # Only the last value will be stored due to collision (no chaining)
    assert ht.get(key1) == "second"
    assert ht.get(key2) == "second"