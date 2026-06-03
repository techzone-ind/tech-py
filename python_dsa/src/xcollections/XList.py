import ctypes

class XList:
    
    def __init__(self):
        self.size = 1
        self.n = 0
        self.A = self.__make_array(self.size)

    def __make_array(self,capacity):
        return (capacity*ctypes.py_object)()
  
    def __len__(self):
        return self.n
    
    def __resize(self,new_capacity):
        resizedArray = self.__make_array(self.size*2)
        self.size = self.size*2
        for i in range(self.n):
            resizedArray[i] = self.A[i]
        self.A = resizedArray

    def __str__(self):
        s = ""
        for i in range(self.n):
            s= s +str(self.A[i])+","
        return "[" + s[:-1] +"]"
    
    def __getitem__(self,index):
        if 0 <= index < self.n:
            return self.A[index]
        else:
            return "Index outof range"
        
    def __delitem__(self,pos):
        if 0 <= pos < self.n:
            for i in range(pos,self.n-1):
                self.A[i] = self.A[i+1]
            self.n = self.n -1

    
    def append(self,input):
        if self.size == self.n:
            self.__resize(self.size*2)
        self.A[self.n] = input
        self.n = self.n +1

    def pop(self):
        if self.n <= 0:
            return "Empty List"
        else:
            self.n = self.n -1

    def clear(self):
        self.n =0
        self.size = 1

    def find(self,value):
        res = -1
        for i in range(self.n):
            if self.A[i] == value:
                res = i
                break
        if res >= 0:
            return res
        else:
            return "Item not found"
        
    def insert(self,pos,item):

        if self.n == self.size:
            self.__resize(self.size*2)

        for i in range(self.n,pos,-1):
            self.A[i] = self.A[i-1]

        self.A[pos] = item
        self.n = self.n +1