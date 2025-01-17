#find_min_max.py
#2018015027 정보통계학과 김한탁
#사용자 정의 함수를 이용해 가장 작은 값과 가장 큰 값 구하기

def find_min_max(A):
    min=A[0]
    max=A[0]
    for i in range(1, len(A)):
        if max < A[i]:
            max = A[i]
        if min > A[i]:
            min = A[i]
    return min, max

data=[5, 3, 8, 4, 9, 1, 6, 2, 7]
x,y = find_min_max(data)
print("(min, max)=", (x,y))