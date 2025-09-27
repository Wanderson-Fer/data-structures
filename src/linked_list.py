"""Singly linked list implementation."""

from typing import Any, Optional, Iterable

class Node:
    """Node of a singly linked list."""
    def __init__(self, data: Any = None, nxt: Optional['Node']=None):
        """
        Initialize a node.

        Args:
            data: Value to store in the node.
            nxt: Reference to the next node.
        """
        self.data: Any = data
        self.nxt: Optional['Node'] = nxt

    def __str__(self) -> str:
        return f'Node(data: "{self.data}")'


class LinkedList:
    """Singly linked list."""
    def __init__(self):
        """Initialize an empty linked list."""
        self.head: Optional['Node'] = None

    def insert_at_beggining(self, data: Any):
        """
        Insert a new node at the beginning of the list.

        Args:
            data: Value to insert.
        """
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        """
        Insert a new node at the end of the list.

        Args:
            data: Value to insert.
        """
        if not self.head:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.nxt:
            itr = itr.nxt
        itr.nxt = Node(data, None)

    def insert_values(self, data_list: Iterable[Any]):
        """
        Insert multiple values into the linked list.

        Args:
            data_list: List of values to insert.
        """
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self) -> int:
        """
        Get the length of the linked list.

        Returns:
            Length of the list.
        """
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.nxt
        return count

    def remove_at(self, index: int) -> None:
        """
        Remove at an specified index

        Args:
            index (int): index of item to be removed
        """
        if not self.head:
            print('Linked list is empty')
            return

        if index < 0 or index >= self.get_length():
            raise IndexError('Out of index')

        if index == 0:
            self.head = self.head.nxt
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1 and itr.nxt:
                itr.nxt = itr.nxt.nxt
                return
            itr = itr.nxt
            count += 1

    def insert_at(self, index: int, data: Any) -> None:
        """
        Insert at an specified position

        Args:
            index (int): position to insert item
        """
        if index < 0 or index > self.get_length():
            raise IndexError('Out of index')

        if index == 0:
            self.insert_at_beggining(data)
            return

        if not self.head:
            print('Linked list is empty')
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.nxt = Node(data, itr.nxt)
                return
            itr = itr.nxt
            count += 1

    def remove_by_value(self, data: Any) -> None:
        """
        Remove item by its value

        Args:
            data (Any): value to be searched
        """
        if not self.head:
            print('Linked list is empty')
            return

        if self.head.data == data:
            self.head = self.head.nxt
            return

        itr = self.head
        while itr.nxt:
            if itr.nxt.data == data:
                itr.nxt = itr.nxt.nxt
                return
            itr = itr.nxt

        print('Value not found"')

    def print(self):
        """Print the linked list elements."""
        if not self.head:
            print('Linked list is empty')
            return
        itr = self.head
        linkedl_str = ''
        while itr:
            linkedl_str += str(itr.data)+'-->'
            itr = itr.nxt
        print(f'head-->{linkedl_str}tail')
