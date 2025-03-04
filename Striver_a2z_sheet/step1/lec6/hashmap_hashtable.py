"""
Hashing is a technique used to map data of arbitrary size to fixed-size values (hash values). In Python, hashing is
primarily implemented using dictionaries (which are hash tables) and the hash() function.

"""
from typing import Any


class HashTable:
    def __init__(self, size):
        # Initialize a table with a fixed size
        self.size = size
        self.table: Any = [None] * size  # we are simply creating empty array of size length

    def hash_function(self, key):
        # Simple hash function: sum of character ASCII values mod table size
        return sum(ord(char) for char in key) % self.size

    def insert(self, key, value):
        # Calculate the hash value (index)
        index = self.hash_function(key)
        # Handle collision using chaining (linked list within a list)
        if self.table[index] is None:
            self.table[index] = []
        # Add the key-value pair to the list
        self.table[index].append((key, value))

    def search(self, key):
        # Calculate the hash value (index)
        index = self.hash_function(key)
        if self.table[index] is not None:
            # Search for the key in the bucket
            for pair in self.table[index]:
                if pair[0] == key:
                    return pair[1]
        return None  # Key not found

    def display(self):
        # Print the entire hash table
        for i, bucket in enumerate(self.table):
            print(f"Index {i}: {bucket}")


# Demonstration
hash_table = HashTable(10)  # Create a hash table of size 10

# Insert key-value pairs
hash_table.insert("apple", 100)
hash_table.insert("banana", 200)
hash_table.insert("grape", 300)
hash_table.insert("orange", 400)
hash_table.insert("pineapple", 500)

# Display the hash table
print("Hash Table:")
hash_table.display()

# Search for keys
print("\nSearching:")
print(f"Value for 'apple': {hash_table.search('apple')}")
print(f"Value for 'banana': {hash_table.search('banana')}")
print(f"Value for 'cherry': {hash_table.search('cherry')}")



