if __name__ == '__main__':
    array = list(map(int, input().rstrip().split()))
    sum = []

    for i in range(0, len(array)):
        value = 0
        for j in range(0, len(array)):
            if i != j:
                value = value + array[j]
        sum.append(value)
    sum.sort()
    print(sum[0], sum[len(array) - 1])
