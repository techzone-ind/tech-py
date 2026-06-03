 

class Node:

    def __init__(self,Value):
        self.data = Value
        self.next = None

class XQueue:

    def __init__(self):
        self.rear = None
        self.front = self.rear
        self.n = 0

    def add(self,value):
        
        new_node = Node(value)
        if self.rear == None:
            self.rear = new_node
            self.front = self.rear
        else:           
            self.rear.next = new_node
            self.rear = new_node
        
        self.n = self.n +1

    def poll(self):
        if self.front == None:
            return "Empty Queue"
        result = self.front.data
        self.front = self.front.next
        self.n = self.n - 1
        return result
    
    def __str__(self):
        result = ""
        temp = self.front
        for i in range(self.n):
            if temp != None:
                result = result +str(temp.data)+"->"
                temp = temp.next

        return result[:-2]

    
         
 