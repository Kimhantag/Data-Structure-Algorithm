# pailndromebyLinkedStack
# 2018015027 김한탁
# 단순연결스택 응용: 회문판단하

class Node:
    def __init__(self, elem, link=None):
        self.data=elem
        self.link=link
        
class LinkedStack:
    def __init__ (self):
        self.top=None
        
    def isEmpty(self):return self.top == None
    def clear(self): self.top = None
        
    def push(self, item):
        n = Node(item, self.top)
        self.top = n
            
    def peek(self):
        if not self.isEmpty():
            return self.top.data
            
    def pop(self):
        if not self.isEmpty():
            n = self.top
            self.top= n.link
            return n.data
        
    def size(self):
        node = self.top
        count=0
        while not node == None:
            node = node.link
            count +=1
        return count
    
    def display(self, msg='Linkedstack:'): 
        print(msg, end="")
        node = self.top기
        while not node == None:
            print(node.data, end=" ")
            node=node.link
        print()

str1=input("문자열을 입력하세요: ")
sentense="".join(filter(str.isalnum,str1))
stack=LinkedStack()
sentense1=[]

for i in range(len(sentense)):
    stack.push(sentense[i].title())
size=stack.size()

for j in range(size):
    sentense1.append(stack.pop())
for s in range(size):
    print("정순출력",sentense1[::-1][s],"역순출력",sentense1[s]," = ",sentense1[::-1][s]==sentense1[s])