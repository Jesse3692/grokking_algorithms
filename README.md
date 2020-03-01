# grokking_algorithms

## 第一章 简介

算法是一组完成任务的指令。

对数：对数运算是幂运算的逆运算。

### 二分查找

二分查找可以简单理解为对半查找，先按照列表的一半的位置判断与期望数字进行比较，如果小的话舍弃右半部分并将中间数值当成最大的数，然后继续进行下一次查找，如果大的话舍弃左半部分并将中间数值当成最小的数，然后继续下一次查找，如果查到最后一个数也不符合则返回`None`。至于代码中的中间值索引加一或者减一是因为之前判断过中间值是否与期望值相同，所以在这个条件不符合时，将这个中间值从下一次判断中排除掉，所以就需要减一加一。

注意：只有当这个查找的列表是有序列表时才管用，而且在运行时计算的只是索引位置并不会产生新的列表。

代码：

[二分查找代码](./s1/binary_search.py)

```python
def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None
```