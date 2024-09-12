import rand


def mergeSort(arr):
    if (len(arr) == 1):
        return arr

    half = len(arr)//2

    return recombine(mergeSort(arr[:half]), mergeSort(arr[half:]))


def recombine(leftArr, rightArr):
    leftIndex = 0
    rightIndex = 0
    mergeArr = [None] * (len(leftArr) + len(rightArr))

    while leftIndex < len(leftArr) and rightIndex < len(rightArr):
        if leftArr[leftIndex] < rightArr[rightIndex]:
            mergeArr[leftIndex + rightIndex] = leftArr[leftIndex]
            leftIndex += 1
        else:
            mergeArr[leftIndex + rightIndex] = rightArr[rightIndex]
            rightIndex += 1

    while leftIndex < len(leftArr):
        mergeArr[leftIndex + rightIndex] = leftArr[leftIndex]
        leftIndex += 1

    while rightIndex < len(rightArr):
        mergeArr[leftIndex + rightIndex] = rightArr[rightIndex]
        rightIndex += 1

    return mergeArr


arr = rand.random_array([None] * 20)
# arr = [5, 3, 2, 1, 8, 10, 11, 9, 23]
arr_out = mergeSort(arr)

print(arr_out)
