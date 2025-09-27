# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=redefined-outer-name

import pytest
from src.linked_list import LinkedList

@pytest.fixture
def ll():
    return LinkedList()

def test_insert_at_beginning(ll):
    ll.insert_at_beggining(10)
    assert ll.head.data == 10
    ll.insert_at_beggining(20)
    assert ll.head.data == 20
    assert ll.head.nxt.data == 10

def test_insert_at_end_empty(ll):
    ll.insert_at_end(5)
    assert ll.head is not None
    assert ll.head.data == 5
    assert ll.head.nxt is None

def test_insert_at_end_non_empty(ll):
    ll.insert_at_beggining(1)
    ll.insert_at_end(2)
    ll.insert_at_end(3)
    # Run until the end to check the order
    current = ll.head
    values = []
    while current:
        values.append(current.data)
        current = current.nxt
    assert values == [1, 2, 3]

