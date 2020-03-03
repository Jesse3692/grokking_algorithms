def find_smallest(arr):
    smallest = arr[0]  # 存储最小值
    smallest_index = 0  # 存储最小值索引

    for i in range(1, len(arr)):
        if arr[i] < smallest:  # 始终保持存储的是最小值
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))  # pop掉原列表最小值并追加到新列表中
    return new_arr

print(selection_sort([5, 4, 1, 3, 6, 7, 8]))