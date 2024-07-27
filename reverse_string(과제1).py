#reverse_string(과제1)
#2018015027 김한탁
#stack을 사용하여, 사용자로부터 입력받은 문자열을
#역순으로 출력하는 프로그램

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

stack=Stack()
string=input("문자열을 입력하세요: ")

for i in range(0, len(string)):
    stack.push(string[i])
    
print("역순으로 출력: ", end="")
for i in range(0, len(string)):
    print(stack.pop(), end="")