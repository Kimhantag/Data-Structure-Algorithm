#check_palindrome by Deque(과제)
#2018015027 김한탁
#Deque를 이용한 회문 구분하기

import string

MAX_QSIZE=10000
class CircularQueue:
    def __init__(self):
        self.front=0
        self.rear=0
        self.items=[None]*MAX_QSIZE
    def isEmpty(self):
        return self.front==self.rear
    def isFull(self):
        return self.front==(self.rear+1)%MAX_QSIZE
    def clear(self):
        self.front=self.rear
    def enqueue(self, item):
        if not self.isFull():
            self.rear=(self.rear+1)%MAX_QSIZE
            self.items[self.rear]=item
    def dequeue(self):
        if not self.isEmpty():
            self.front=(self.front+1)%MAX_QSIZE
            return self.items[self.front]
    def peek(self):
        if not self.isEmpty():
            return self.items[(self.front+1)%MAX_QSIZE]
    def size(self):
        return (self.rear-self.front+MAX_QSIZE)%MAX_QSIZE
    def display(self):
        out=[]
        if self.front<self.rear:
            out=self.items[self.front+1:self.rear+1]
        else:
            out=self.items[self.front+1:MAX_QSIZE]\
                +self.items[0:self.rear+1]
        print("[f=%s,r=%d]==>" %(self.front,self.rear),out)

        
class CircularDeque(CircularQueue):
    def __init__(self):
        super().__init__()
    def addRear(self,item):
        self.enqueue(item)
    def deleteFront(self):
        return self.dequeue()
    def getFront(self):
        return self.peek()
    def addFront(self,item):
        if not self.isFull():
            self.items[self.front]=item
            self.front=self.front-1
            if self.front<0 :
                self.front=MAX_QSIZE-1
    def deleteRear(self):
        if not self.isEmpty():
            item=self.items[self.rear]
            self.rear=self.rear-1
            if self.rear<0:
                self.rear=MAX_QSIZE-1
            return item
    def getRear(self):
        return self.items[self.rear]

class Stack:
    def __init__(self):
        self.top=[]
    
    def isEmpty(self): return len(self.top)==0
    def size(self): return len(self.top)
    def clear(self): self.top=[]

    def push(self, item):
        self.top.append(item)
        
    def pop(self):
        if not self.isEmpty():
            return self.top.pop(-1)
    
    def peek(self):
        if not self.isEmpty():
            return self.top[-1]
        
    def __str__ (self):
        return str(self.top[::-1])

def palind(sentence):
    cir_Deque1=CircularDeque()
    cir_Deque2=CircularDeque()
    sentence=list(sentence.lower())
    
    for ch in sentence[::]:
        if ch in string.punctuation or ch in " ":
            sentence.remove(ch)            
        else:
            cir_Deque1.addRear(ch)
            cir_Deque2.addRear(ch)            
    
    for i in range(0, len(sentence)):
        Front_Deque = cir_Deque1.deleteFront()
        Rear_Deque = cir_Deque2.deleteRear()
        
        if Front_Deque == Rear_Deque:
            print(Front_Deque,"==",Rear_Deque)
            
            if i == len(sentence)-1 :
                return "회문입니다"
                break
            else:
                continue              
        else:
            print(Front_Deque,"!=",Rear_Deque)
            return "회문아닙니다."
            break

print(palind("eye"))
print(palind("ey_e"))
print(palind("ey_E"))
print(palind("eyE"))
print(palind("ey_el"))
