
class Node:

    def __init__(self,value):
        self.data = value
        self.next = None

class XStack:

    def __init__(self):
        self.top = None
        self.n = 0

    def isempty(self):
        return self.top == None

    def push(self,value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.n = self.n + 1
          

    def pop(self):
        if self.top == None:
            return 'Empty Stack'
        result = self.top.data
        self.top = self.top.next
        self.n = self.n - 1
        return result
    
    def peek(self):
        if self.isempty():
            return "Empty Stack"
        else:
            return self.top.data
    

    def __str__(self):
        result = ""
        temp = self.top
        for i in range(self.n):
            if temp != None:
                result = result +str(temp.data)+"->"
                temp = temp.next

        return result[:-2]
    
    def size(self):
        return self.n
