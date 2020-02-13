def bigSum(array):
    value = 0
    for i in array:
        value = value + i
    return value


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    print(bigSum(arr))
