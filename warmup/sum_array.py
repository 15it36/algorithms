def solveArray(arr):
    value = 0
    for i in range(len(arr)):
        value = value + arr[i]
    return value


arr_count = int(input())
arr = list(map(int, input().rstrip().split()))
result = solveArray(arr)
print(result)
