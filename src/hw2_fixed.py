"""Module providing a function to perform Merge Sort"""

import rand


def merge_sort(arr_merge):
    """Function to perform the merging"""
    if len(arr_merge) == 1:
        return arr_merge

    half = len(arr_merge) // 2

    return recombine(merge_sort(arr_merge[:half]), merge_sort(arr_merge[half:]))


def recombine(left_arr, right_arr):
    """Correct implementation of recombine function"""
    left_index = 0
    right_index = 0
    merge_arr = [None] * (len(left_arr) + len(right_arr))

    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            merge_arr[left_index + right_index] = left_arr[left_index]
            left_index += 1
        else:
            merge_arr[left_index + right_index] = right_arr[right_index]
            right_index += 1

    while left_index < len(left_arr):
        merge_arr[left_index + right_index] = left_arr[left_index]
        left_index += 1

    while right_index < len(right_arr):
        merge_arr[left_index + right_index] = right_arr[right_index]
        right_index += 1

    return merge_arr


arr = rand.random_array([None] * 20)
# arr = [5, 3, 2, 1, 8, 10, 11, 9, 23]
arr_out = merge_sort(arr)

print(arr_out)
