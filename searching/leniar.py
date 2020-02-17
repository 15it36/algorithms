""" Linear search """

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    for value in arr:
        if value == n:
            print(value)
