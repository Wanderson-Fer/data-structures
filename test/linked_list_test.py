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

def test_insert_list_of_values(ll):
    ll.insert_values([1, 2, 3, 4])
    current = ll.head
    values = []
    while current:
        values.append(current.data)
        current = current.nxt
    assert values == [1, 2, 3, 4]

def test_insert_empty_list(ll):
    ll.insert_values([])
    assert ll.head is None

def test_insert_dict_values(ll):
    ll.insert_values([{1: 'a'}, {2: 'b'}, {3: 'c'}])
    current = ll.head
    values = []
    while current:
        values.append(current.data)
        current = current.nxt
    assert values == [{1: 'a'}, {2: 'b'}, {3: 'c'}]

def test_get_length_empty(ll):
    assert ll.get_length() == 0

def test_get_length_non_empty(ll):
    ll.insert_at_beggining(1)
    ll.insert_at_beggining(2)
    ll.insert_at_beggining(3)
    assert ll.get_length() == 3

def test_remove_at_empty_list(ll, capsys):
    ll.remove_at(0)
    captured = capsys.readouterr()
    assert 'Linked list is empty' in captured.out

def test_remove_at_last_item(ll):
    ll.insert_values([10])
    ll.remove_at(0)
    assert ll.head is None

def test_remove_at_last_item_multiple(ll):
    ll.insert_values([1, 2, 3])
    ll.remove_at(2)
    current = ll.head
    values = []
    while current:
        values.append(current.data)
        current = current.nxt
    assert values == [1, 2]

def test_remove_at_non_empty(ll):
    ll.insert_values([1, 2, 3, 4])
    ll.remove_at(2)
    current = ll.head
    values = []
    while current:
        values.append(current.data)
        current = current.nxt
    assert values == [1, 2, 4]

def test_remove_at_first_item(ll):
    ll.insert_values([100, 200, 300])
    ll.remove_at(0)
    current = ll.head
    values = []
    while current:
        values.append(current.data)
        current = current.nxt
    assert values == [200, 300]

