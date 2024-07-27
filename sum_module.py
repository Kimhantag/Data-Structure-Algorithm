#sum_module.py
#2018015027 정보통계학과 김한탁
#반복문을 이용하여 sum값을 구한 뒤 반환하는 사용자 정의 함수  

def sum_range(begin, end, step=1):
    sum = 0
    for n in range(begin, end, step):
        sum += n
    return sum

