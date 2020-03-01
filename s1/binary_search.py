def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high: # 只有列表中最大值小于或等于最大值时程序才运行
        mid = (low + high) // 2  # 根据最大值和最小值的索引运算出中间值的索引
        guess = list[mid]  
        if guess == item:  # 如果中间值等于期望值，返回中间值
            return mid
        elif guess > item:  # 如果中间值大于期望值，修改最大值索引
            high = mid - 1
        else:  # 如果中间值小于期望值，修改最小值索引
            low = mid + 1
    return None


my_list = [1, 3, 4, 6, 7, 9, 11, 13]
print(binary_search(my_list, 3))
