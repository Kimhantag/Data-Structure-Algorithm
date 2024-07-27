# 2. 팩토리얼 순환함수 구현
def factorial(n):
    if n==1 :
        return 1
    else :
        return n*factorial(n-1)
print(factorial(5))
    
# 2.1 팩토리얼 반복함수 구현
def factorial1(n):
    result=1
    for i in range(1, n+1):
        result = result*i
    return result
    
print(factorial1(5))