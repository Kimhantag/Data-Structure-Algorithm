#find_max.py
#2018015027 정보통계학과 김한탁
#사용자 정의 함수를 이용하여 가장 큰 값 구하기

def find_max(A):
    max = A[0]
    for i in range(1, len(A)):
        if max < A[i]:
            max = A[i]
    return max

data = [5, 3, 8, 4, 9, 1, 6, 2, 7]
print("max = ", find_max(data))
    