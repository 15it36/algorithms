if __name__ == '__main__':
    n = int(input())
    index = 1

    for i in range(1, n + 1):
        print(str('#'*i).rjust(n))
