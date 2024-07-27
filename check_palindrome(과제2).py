#check_palindrome(과제2)
#2018015027 김한탁
#스택을 이용하여 회문인지 확인하는 프로그램

import string

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

def check_palindrome(sentence):
    stack=Stack()    

    for ch in sentence[::]:
        if ch in string.punctuation or ch in " ":
            sentence.remove(ch)
        else:
            stack.push(ch)

    for i in range(0, len(sentence)):
        reverse_ch=stack.pop()
        
        if sentence[i] == reverse_ch:
            print(sentence[i],"==",reverse_ch)
            
            if i == len(sentence)-1:
                print("회문입니다.")
                break
            else:
                continue                     
        else:
            print(sentence[i],"!=",reverse_ch)
            print("따라서 회문이 아닙니다.")
            break

input_string=list(input("문자열을 입력하세요: ").lower())         
check_palindrome(input_string)