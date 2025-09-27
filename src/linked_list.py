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

