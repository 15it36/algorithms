""" Binary search """


def binary_search(l, r, array, x):
    """
    Binary search
    :param l: Integer
    :param r: Integer
    :param array: Array
    :param x: Integer
    :return: Index from array
    """
    mid = (l + r) / 2
    if x == array[mid]:
        return mid
    if x > array[mid]:
        return binary_search(l, mid - 1, array, x)
    return binary_search(mid + 1, r, array, x)


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    value = int(input())
    arr.sort()
    left = 0
    right = len(arr)
    mid = len(arr) / 2
    if value > arr[mid]:
        left = mid
        right = len(arr)
    elif value < arr[mid]:
        left = 0
        right = mid
    elif value == arr[mid]:
        print(value, "Is present in array")
    print(binary_search(left, right, arr, value))
