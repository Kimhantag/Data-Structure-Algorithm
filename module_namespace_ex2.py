#module_namespace_ex2.py
#2018015027 정보통계학과 김한탁
#모듈의 함수를 이용하여 최소, 최댓값과 sum을 구하기(방법2)

from min_max_module import *
from sum_module import *

data=[5, 3, 8, 4, 9, 1, 6, 2, 7]
print("(min, max)=", find_min_max(data))
print("sum = ", sum_range(1, 10))