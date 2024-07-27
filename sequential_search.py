#sequential search
#2018015027 김한탁
#순차탐색 알고리즘

def sequential_search(A, key, low, high):
    for i in range(low, high+1):
        if A[i] == key:
            return i
    return None

data=[5, 3, 8, 4, 9, 1, 6, 2, 7]
print(sequential_search(data, 6, 0, 8))

