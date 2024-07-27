#min_max_module.py
#2018015027 정보통계학과 김한탁
#가장 작은 값과 가장 큰 값을 반복문을 이용하여 구한 뒤 반환하는 사용자 정의 함수

def find_min_max(A):
    min=A[0]
    max=A[0]
    for i in range(1, len(A)):
        if max < A[i]:
            max = A[i]
        if min > A[i]:
            min = A[i]
    return min, max

