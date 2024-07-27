# 3. 피보나치 수열 반복문 구현
def fib_iter(n) :
    if(n < 2):
        return n
    
    last=0
    current=1
    for i in range(2, n+1):
        tmp = current
        current += last
        last = tmp
    return current
print(fib_iter(6))

# 3.1 피보나치 수열 순환 함수
def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
print(fibo(6))