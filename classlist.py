import ctypes

class MYLIST:
    def __init__(self):
        self.size=1
        self.n=0
        #create a c types array
        self.A=self.__make_array(self.size)
    #length function
    def __len__(self):
        return(self.n)
    def __getitem__(self,index):
        if 0<=index<self.n:
            return self.A[index]
        else:
            return 'index error -out of range'
    
    def pop(self):
        if self.n==0:
            print("empty list")
        else:
            print(self.A[self.n-1])
            self.n=self.n-1
    
    def clear(self):
        self.n=0
        self.size=1
    def __str__(self):
        res=''
        for i in range(self.n):
            res=res+str(self.A[i])+','
        return '['+res[:-1]+']'

    def append(self,item):
        if self.n==self.size:
            self.__resize(self.size*2)
        
        self.A[self.n]=item
        self.n=self.n+1
    
    def __resize(self,new_capacity):
        B=self.__make_array(new_capacity)
        self.size=new_capacity
        #copy from A
        for i in range(self.n):
            B[i]=self.A[i]
        self.A=B
    
    def __make_array(self,capacity):
#create a c types array(static,refrential) with size=capacity
        return (capacity*ctypes.py_object)()

obj=MYLIST()
print(obj)
print("length of list:",len(obj))

obj.append(2)
obj.append(2)
obj.append(2)
obj.append(2)
print(obj)
print("length of list:",len(obj))

obj.pop()
print(obj)
print(obj[2])
print(obj[7])