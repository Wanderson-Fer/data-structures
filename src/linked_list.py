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

