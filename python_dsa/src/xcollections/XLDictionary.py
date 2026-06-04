
# -----------------------------------------------------------------------------
# Script Name: XLDictionary.py
# Author:      Animesh Sinha
# Description: Dictionary bucket linked list implementation.
# --

class Node:

    def __init__(self,key,value):
        self.key = key
        self.value = value 
        self.next = None

class LL:
    """Performs the actual bucket linked list implementation

        This makes it possible to add hash collision value at same index.
        """

    def __init__(self):
        self.head = None
        self.n = 0

    def insert(self,key,value):
        if self.head == None:
            new_node = Node(key,value)
            self.head = new_node
            self.n = self.n + 1
        else:
            new_node = Node(key,value)
            curr_node = self.head
            for i in range(self.n):
                if(curr_node.next == None):
                    curr_node.next = new_node
                    self.n = self.n +1
                    break
                #print(curr_node.data)
            curr_node = curr_node.next

    def size(self):
        return self.n
    
    def traverse(self):
        """ Traverse and explore data in list   """
        curr_node = self.head

        for i in range(self.n):
            if(curr_node == None):
                print(str(curr_node.key)+ " "+curr_node.value)
                curr_node = curr_node.next
                break
    
    def __str__(self):
        curr_node = self.head
        res = ''
        for i in range(self.n):
            if(curr_node == None):
                break
            res = res + str(curr_node.key)+"->"+ str(curr_node.value)+" "
            curr_node = curr_node.next

        return res
            

class XLDictionary:
    """LinkedList implementaion for Dictionary
        Allow add value at same index when hash collision arrived
    """

    def __init__(self,capacity):
        self.capacity = capacity
        self.bucket = self.make_ll(self.capacity)
    
    def make_ll(self,capacity):
        bucket = []
        for i in range(capacity):
            bucket.append(LL())

        return bucket
    
    def hashing(self,key):
        return abs(hash(key)) % self.capacity
    
    def put(self,key,value):
        bucket_index = self.hashing(key)
        self.bucket[bucket_index].insert(key,value)


