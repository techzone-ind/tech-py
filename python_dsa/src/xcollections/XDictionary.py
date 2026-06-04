
# -----------------------------------------------------------------------------
# Script Name: XDictionary.py
# Author:      Animesh Sinha
# Description: Dictionary array bucket implementation.
# --
class XDictionary:
    """Performs array bucket implementation
        """

    def __init__(self, size):
        self.size = size
        self.bucket = [None] * self.size
        self.data = [None] * self.size

    def hashing(self,key):
        return abs(hash(key)) % self.size
    
    def rehashing(self,old_index_hash):
        return (old_index_hash + 1) % self.size
    
    def put(self,key,value):
        hash_index = self.hashing(key)

        if self.bucket[hash_index] == None:
            self.bucket[hash_index] = key
            self.data[hash_index] = value
        else:
            if self.bucket[hash_index] == key:
                self.data[hash_index] = value
            else:
                rehash_index = self.rehashing(hash_index)
                while self.bucket[rehash_index] != None and self.bucket[rehash_index] != key:
                    rehash_index = self.rehashing(rehash_index)

                if self.bucket[rehash_index] == None:
                    self.bucket[rehash_index] = key
                    self.data[rehash_index] = value
                else:
                    self.data[rehash_index] = value

    def __setitem__(self,key,value):
        self.put(key,value)

    def get(self,key):
        hash_index = self.hashing(key)
        curr_index = hash_index

        while self.bucket[curr_index] != None:
            if self.bucket[curr_index] == key:
                return self.data[curr_index]
            
            curr_index = self.rehashing(curr_index)

            if curr_index == hash_index:
                return "Key not found"
            
        return "Not found"

    def __getitem__(self,key):
        return self.get(key)