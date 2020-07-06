"""
Hash maps are efficient key-value stores. 
They are capable of assigning and retrieving data in the fastest way possible for a data structure.
This is because the underlying data structure that they use is an array.
A value is stored at an array index determined by plugging the key into a hash function.

In Python we don’t have an array data structure that uses a contiguous block of memory.
We are going to simulate an array by creating a list and keeping track of the size of the list 
with an additional integer variable. This will allow us to design something that resembles a hash map.
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

    def hash(self, key, count_collisions=0):  # hash Fn
        key_bytes = key.encode()
        hash_code = sum(key_bytes)
        return hash_code + count_collisions

    def compressor(self, hash_code):  # compresses the hash Fn
        return hash_code % self.array_size

    # Assigning the value based on key.
    def assign(self, key, value):  # Setter Fn
        array_index = self.compressor(self.hash(key))
        current_array_value = self.array[array_index]

        # check if possible_return_value is None. If so, return None.
        if current_array_value is None:
            self.array[array_index] = [key, value]
            return
        # if the first element in possible_return_value (index 0) is the same as key.
        # If so, return possible_return_value[1], the value.
        if current_array_value[0] == key:
            self.array[array_index] = [key, value]
            return

        # Collision
        number_collisions = 1

        while(current_array_value[0] != key):
            new_hash_code = self.hash(key, number_collisions)
            new_array_index = self.compressor(new_hash_code)
            current_array_value = self.array[new_array_index]

            if current_array_value is None:
                self.array[new_array_index] = [key, value]
                return

            if current_array_value[0] == key:
                self.array[new_array_index] = [key, value]
                return

            number_collisions += 1

        return

    # It calculates the array index in the same way our .assign() does and then retrieve the value at that index.
    def retrieve(self, key):
        array_index = self.compressor(self.hash(key))
        possible_return_value = self.array[array_index]

        if possible_return_value is None:
            return None

        if possible_return_value[0] == key:
            return possible_return_value[1]

        retrieval_collisions = 1
        while (possible_return_value[0] != key):
            new_hash_code = self.hash(key, retrieval_collisions)
            retrieving_array_index = self.compressor(new_hash_code)
            possible_return_value = self.array[retrieving_array_index]

            if possible_return_value is None:
                return None

            if possible_return_value[0] == key:
                return possible_return_value[1]

            retrieval_collisions += 1


hash_map = HashMap(20)
hash_map.assign("gneiss", "metamorphic")
print(hash_map.retrieve("gneiss"))

hash_map = HashMap(15)
hash_map.assign('gabbro', 'igneous')
hash_map.assign('sandstone', 'sedimentary')
hash_map.assign('gneiss', 'metamorphic')

print(hash_map.retrieve('gabbro'))
print(hash_map.retrieve('sandstone'))
print(hash_map.retrieve('gneiss'))
