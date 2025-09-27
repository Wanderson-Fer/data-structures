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


