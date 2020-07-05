"""
Hash maps are efficient key-value stores. 
They are capable of assigning and retrieving data in the fastest way possible for a data structure.
This is because the underlying data structure that they use is an array.
A value is stored at an array index determined by plugging the key into a hash function.

In Python we don’t have an array data structure that uses a contiguous block of memory.
We are going to simulate an array by creating a list and keeping track of the size of the list 
with an additional integer variable.This will allow us to design something that resembles a hash map.
This is somewhat elaborate for the actual storage of a key-value pair, but it helps to remember that 
the purpose of this lesson is to gain a deeper understanding of the structure as it is constructed.
For real-world use cases in which a key-value store is needed, Python offers a built-in hash table 
implementation with dictionaries.
"""


class HashMap:

    # Implementing by simulating array like structure
    def __init__(self, array_size):
        self.array_size = array_size
        # Making a Null array with 'array_size' length
        self.array = [None for item in range(array_size)]

    def hash(self, key):  # hash Fn
        key_bytes = key.encode()
        hash_code = sum(key_bytes)
        return hash_code

    def compressor(self, hash_code):  # compresses the hash Fn
        return hash_code % self.array_size

    # Assigning the value based on key.
    def assign(self, key, value):  # Setter Fn
        self.array[self.compressor(self.hash(key))] = value

    # It calculates the array index in the same way our .assign() does and then retrieve the value at that index.
    def retrieve(self, key):
        return self.array[self.compressor(self.hash(key))]


hash_map = HashMap(20)
hash_map.assign("gneiss", "metamorphic")
print(hash_map.retrieve("gneiss"))
