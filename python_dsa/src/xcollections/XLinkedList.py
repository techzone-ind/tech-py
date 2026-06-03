
class Node:

    def __init__(self,value):
        self.data = value
        self.next = None


class XLinkedList:

    def __init__(self):
        self.head =None
        self.n =0

    def __len__(self):
        return self.n
    
    def insert_head(self,value):
        new_node = Node(value)

        new_node.next = self.head
        self.head = new_node
        self.n = self.n +1

    def append(self,value):
        new_node = Node(value)
        curr_node = self.head
        for i in range(self.n):
            if(curr_node.next == None):
                curr_node.next = new_node
                self.n = self.n +1
                break
            print(curr_node.data)
            curr_node = curr_node.next
      
    def insert_after(self,after,value):
        new_node = Node(value)
        curr_node = self.head
        for i in range(self.n):
            if(curr_node.data == after):
                new_node.next = curr_node.next
                curr_node.next = new_node
                self.n = self.n +1
                break
            curr_node = curr_node.next

    def traverse(self):
        curr_node = self.head

        for i in range(self.n):
            if(curr_node == None):
                print(curr_node.data)
                curr_node = curr_node.next
                break
            

    def __str__(self):
        curr_node = self.head
        res = ''
        for i in range(self.n):
            if(curr_node == None):
                break
            res = res + str(curr_node.data)+"->"
            curr_node = curr_node.next

        return res[:-2]

