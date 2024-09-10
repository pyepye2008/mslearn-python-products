
import numpy as np

#请写一段冒泡查询代码  
#昌泡查询法 。它重复地走访要排序的数列，一次比较两个元素，如果它们的顺序错误就把它们交换过来。
def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n-1):
        for j in range(0, n-i-1):  #从0到n-i-1 star,stop
            if arr[j] > arr[j+1]:
                #两个相邻的数值互换
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr = [64, 34, 25, 12, 22, 11, 90]

#昌泡查询法调用
print(bubble_sort(arr))  

arr_sort = [80, 74, 25, 12, 22, 11, 90]
print(np.sort(arr_sort))

