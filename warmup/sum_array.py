def solveArray(array):
    value = 0
    for i in range(len(array)):
        value = value + array[i]
    return value


arr_count = int(input())
arr = list(map(int, input().rstrip().split()))
result = solveArray(arr)
print(result)
