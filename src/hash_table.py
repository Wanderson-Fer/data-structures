class HashTable:
    """Simple hash table implementation using string keys."""

    def __init__(self, size: int) -> None:
        """
        Initialize the hash table.

        Args:
            size: Number of slots in the table.
        """
        self.max = size | 100
        self.arr = [None for i in range(self.max)]

    def get_hash(self, key: str) -> int:
        """
        Compute hash value for a given key.

        Args:
            key: String key.

        Returns:
            Hash index for the key.
        """
        h = 0
        for char in key:
            h += ord(char)
        return h % self.max

    def add(self, key: str, value):
        """
        Add a key-value pair to the hash table.

        Args:
            key: String key.
            value: Value to store.
        """
        h = self.get_hash(key)
        self.arr[h] = value

    def get(self, key: str):
        """
        Retrieve value by key.

        Args:
            key: String key.

        Returns:
            Value associated with the key.
        """
        h = self.get_hash(key)
        return self.arr[h]
