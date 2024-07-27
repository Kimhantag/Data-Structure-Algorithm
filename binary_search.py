#binary search
#2018015027 김한탁
#이진탐색 알고리즘

def binary_search(A, key, low, high):
    if (low <= high):
        middle = (low + high) // 2
        if key == A[middle]:
            return middle
        elif (key < A[middle]):
            return binary_search(A, key, low, middle-1)
        else:
            return binary_search(A, key, middle+1, high)
    return None
        
data=[1,2,3,4,5,6,7,8,9]
print(binary_search(data, 2, 0, len(data)))