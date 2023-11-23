# HASHMAP: indexed data structures with key, value pairs with no duplicates (dictionary)

# The hash map design will include the following functions:
#  set_val(key, value): Inserts a key-value pair into the hash map. If the value already exists in the hash map,
#                        update the value.
#  get_val(key): Returns the value to which the specified key is mapped, or “No record found” if this map contains
#                        no mapping for the key.
#  delete_val(key): Removes the mapping for the specific key if the hash map contains the mapping for the key.

# HASH FUNCTION:
'''
print("Hash Function:")
for char in key:
    hash += ord(char)
hash %= 5
'''

# HASH MAP:
print("HASH MAP:\n")
class HashMap:
    def __init__(self):
        self.size = 6
        self.map = [None] * self.size

    def _get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.size

    def add(self, key, value):
        key_hash = self._get_hash(key)
        key_value = [key, value]

        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.map[key_hash].append(key_value)
            return True

    def get(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        key_hash = self._get_hash(key)

        if self.map[key_hash] is None:
            return False
        for i in range(0, len(self.map[key_hash])):
            if self.map[key_hash][i][0]==key:
                self.map[key_hash].pop(i)
                return True

    def print(self):
        print("---Phonebook---")
        for item in self.map:
            if item is not None:
                print(str(item))

hashmap = HashMap()
hashmap.add('Kevin', '630-890-5069')
hashmap.add('Fides', '630-890-4928')
hashmap.add('Kyle', '630-890-4916')
hashmap.add('Jasmine', '630-890-5656')
hashmap.add('Lily', '630-167-5692')
hashmap.add('Peter', '630-123-6534')
hashmap.print()
hashmap.delete('Jasmine')
print("\nDeleting Jasmine:")
hashmap.print()

print(f"\nGetting Kevin's number:\nKevin: {hashmap.get('Kevin')}")

print("----------------------------------------")
print()

# HASH TABLE:
print("HASH TABLE: \n")


class HashTable:

    # Create empty bucket list of given size
    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_buckets()

    def create_buckets(self):
        return [[] for _ in range(self.size)]

    # Insert values into hash map
    def set_val(self, key, val):

        # Get the index from the key
        # using hash function
        hashed_key = hash(key) % self.size

        # Get the bucket corresponding to index
        bucket = self.hash_table[hashed_key]

        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record

            # check if the bucket has same key as
            # the key to be inserted
            if record_key == key:
                found_key = True
                break

        # If the bucket has same key as the key to be inserted,
        # Update the key value
        # Otherwise append the new key-value pair to the bucket
        if found_key:
            bucket[index] = (key, val)
        else:
            bucket.append((key, val))

    # Return searched value with specific key
    def get_val(self, key):

        # Get the index from the key using
        # hash function
        hashed_key = hash(key) % self.size

        # Get the bucket corresponding to index
        bucket = self.hash_table[hashed_key]

        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record

            # check if the bucket has same key as
            # the key being searched
            if record_key == key:
                found_key = True
                break

        # If the bucket has same key as the key being searched,
        # Return the value found
        # Otherwise indicate there was no record found
        if found_key:
            return record_val
        else:
            return "No record found"

    # Remove a value with specific key
    def delete_val(self, key):

        # Get the index from the key using
        # hash function
        hashed_key = hash(key) % self.size

        # Get the bucket corresponding to index
        bucket = self.hash_table[hashed_key]

        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record

            # check if the bucket has same key as
            # the key to be deleted
            if record_key == key:
                found_key = True
                break
        if found_key:
            bucket.pop(index)
        return

    # To print the items of hash map
    def __str__(self):
        return "".join(str(item) for item in self.hash_table)


hash_table = HashTable(50)

# insert some values
hash_table.set_val('Kevin', 'kevin27@gmail.com')
print(hash_table)
print()

hash_table.set_val('Jasmine', 'jas_04@yahoo.com')
print(hash_table)
print()

# search/access a record with key
print(hash_table.get_val('Kevin'))
print()

# delete or remove a value
hash_table.delete_val('Jasmine')
print(hash_table)