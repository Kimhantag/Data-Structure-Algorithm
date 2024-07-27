#Stack(function)
#2018015027 김한탁
#스택의 구현 (함수버전)

top=[]
def isEmpty():
    return len(top) == 0
def push(item):
    top.append(item)
def pop():
    if not isEmpty():
        return top.pop(-1)
def peek():
    if not isEmpty():
        return top[-1]
def size(): 
    return len(top)
def clear():
    global top
    top=[]

for i in range(1, 6):
    push(i)
print('push 5회: ', top)
print('pop() --> ', pop())
print('pop() --> ', pop())
print('pop 2회 ', top)

print('pop 2회 ', top)
push("홍길동")
push("이순신")
print('push +2회: ', top)
print('pop() --> ', pop())
print('pop 1회 ', top)