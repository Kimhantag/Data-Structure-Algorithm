#module_namespace_ex1.py
#2018015027 정보통계학과 김한탁
#모듈의 함수를 이용하여 최소, 최댓값과 sum을 구하기(방법1)

import min_max_module
import sum_module

data=[5, 3, 8, 4, 9, 1, 6, 2, 7]
print("(min, max)=", min_max_module.find_min_max(data))
print("sum = ", sum_module.sum_range(1, 10))

from math import pow, sqrt
result = pow(2, 10)
dist=sqrt(1000)
