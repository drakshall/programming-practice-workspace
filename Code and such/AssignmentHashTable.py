class HashTable:                                    
    def __init__(self, size):                                       # Size of table manually specified
        self.size = size
        self.table = [[] for _ in range(size)]

    def hashMeth(self, key):
        # charSum = 0                                               # Original hash function summing character ASCII values.
        # for char in key:                                          # Switched out for python's hash function because of poor distribution.
        #     charSum += ord(char)
        # return charSum % self.size
        return hash(key) % self.size

    def insert(self, key, value):                                   # Uses the hash method to hash the key of an input tuple and loads both  
        index = self.hashMeth(key)                                  # values into the index associated with the hashed key scaled to the 
        bucket = self.table[index]                                  # size of the table.
        for i, (existingKey, _) in enumerate(bucket):
            if existingKey == key:                                  # If the key is already present updates the entry.
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
 
    def retrieve(self, key):                                        # Uses the hash method to hash a key and find the index where the associated
        index = self.hashMeth(key)                                  # tuple is stored then compares the query key with the key(s) in that index
        bucket = self.table[index]                                  # until a match is found then returns that associated value.
        for existingKey, existingValue in bucket:
            if existingKey == key:
                return existingValue
        raise KeyError(f"Key '{key}' not found")
    
    def delete(self, key):                                          # Uses the hash method to hash a key and find the index where the associated
        index = self.hashMeth(key)                                  # tuple is stored then compares the query key with the key(s) in that index
        bucket = self.table[index]                                  # until a match is found then pops that value out of the array.
        for i, (existingKey, _) in enumerate(bucket):
            if existingKey == key:
                deletedValue = bucket.pop(i)[1]
                return deletedValue
        raise KeyError(f"Key '{key}' not found")
    
    def listEntries(self):                                          # Iterates through the hash table to make a list of every tuple then prints it.
        allEntries = []
        for bucket in self.table:
            for key, value in bucket:
                allEntries.append((key, value))
        return print(allEntries)
    
    def analytics(self):
        chainLengths = [len(bucket) for bucket in self.table]               # Measures and prints various metrics of the hash table.
        bucketCount = len(chainLengths)
        emptyBucketCount = sum(1 for length in chainLengths if length == 0)
        nonemptyBucketCount = bucketCount - emptyBucketCount
        maxChain = max(chainLengths) if chainLengths else 0
        minChain = min(chainLengths) if chainLengths else 0
        entryCount = sum(chainLengths)
        loadFactor = entryCount / bucketCount
        print(f"Bucket Count: {bucketCount}")
        print(f"Empty Buckets: {emptyBucketCount}")
        print(f"Occupied Buckets: {nonemptyBucketCount}")
        print(f"Max Chain Length: {maxChain}")
        print(f"Min Chain Length: {minChain}")
        print(f"Total Entries: {entryCount}")
        print(f"Load Factor: {loadFactor}")
        print(f"List of chain lengths: {chainLengths}")
        return

import unittest

class TestHashTable(unittest.TestCase):         # note - all unit tests are machine generated
    
    def setUp(self):
        """Create a fresh HashTable instance before each test"""
        self.ht = HashTable(5)
    
    def test_insert_and_retrieve(self):
        """Test basic insertion and retrieval of a key-value pair"""
        self.ht.insert("name", "Alice")
        self.assertEqual(self.ht.retrieve("name"), "Alice")
    
    def test_insert_update_existing_key(self):
        """Test that inserting with an existing key updates the value"""
        self.ht.insert("name", "Alice")
        self.ht.insert("name", "Bob")  # Should overwrite "Alice"
        self.assertEqual(self.ht.retrieve("name"), "Bob")
    
    def test_retrieve_nonexistent_key(self):
        """Test that retrieving a missing key raises KeyError"""
        with self.assertRaises(KeyError):
            self.ht.retrieve("unknown")
    
    def test_delete_existing_key(self):
        """Test deletion of an existing key and verify it's removed"""
        self.ht.insert("name", "Alice")
        deleted = self.ht.delete("name")
        self.assertEqual(deleted, "Alice")  # Should return deleted value
        
        # Verify key no longer exists
        with self.assertRaises(KeyError):
            self.ht.retrieve("name")
    
    def test_delete_nonexistent_key(self):
        """Test that deleting a missing key raises KeyError"""
        with self.assertRaises(KeyError):
            self.ht.delete("unknown")
    
    def test_collision_handling(self):
        """
        Test that multiple keys hashing to same bucket are handled correctly.
        Uses a small table size (5) to increase collision probability.
        """
        self.ht.insert("abc", 1)
        self.ht.insert("acb", 2)  # Likely collides with "abc" in same bucket
        
        # Both values should be retrievable despite collision
        self.assertEqual(self.ht.retrieve("abc"), 1)
        self.assertEqual(self.ht.retrieve("acb"), 2)
    
    def test_multiple_operations_sequence(self):
        """
        Test a realistic sequence of mixed operations to ensure
        the hash table maintains consistency across multiple actions.
        """
        # Insert multiple keys
        self.ht.insert("a", 1)
        self.ht.insert("b", 2)
        self.ht.insert("c", 3)
        
        # Delete middle key
        self.ht.delete("b")
        
        # Remaining keys should be intact
        self.assertEqual(self.ht.retrieve("a"), 1)
        self.assertEqual(self.ht.retrieve("c"), 3)
        
        # Deleted key should be gone
        with self.assertRaises(KeyError):
            self.ht.retrieve("b")

# unittest.main()

import time
import random
import string

start = time.time()

Table = HashTable(9999)
length = 16
keyCount = 9999
for i in range(keyCount):
    randomKey = ''.join(random.choices(string.ascii_letters, k=length))
    randomValue = random.randint(0, 20000)
    Table.insert(randomKey, randomValue)
Table.analytics()
#Table.listEntries()

end = time.time()
print(f"Total runtime of the program is {end - start} seconds")
with open("TimeLog.txt", "a") as f:
  f.write(f"{end - start}\n")
