def compareTriplets(first_array, second_array):
    bob = alice = 0
    for i in range(len(first_array)):
        if first_array[i] > second_array[i]:
            alice = alice + 1
        if second_array[i] > first_array[i]:
            bob = bob + 1

    return alice, bob


if __name__ == '__main__':
    arr_1 = list(map(int, input().rstrip().split()))

    arr_2 = list(map(int, input().rstrip().split()))

    print(compareTriplets(arr_1, arr_2))
