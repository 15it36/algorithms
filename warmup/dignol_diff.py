""" Diagonal subtraction """

if __name__ == '__main__':
    n = int(input())

    matrix = []
    diagonal = in_diagonal = 0
    for _ in range(n):
        matrix.append(list(map(int, input().rstrip().split())))
    for i in range(n):
        for j in range(n):
            if i == j:
                diagonal += matrix[i][j]
            if i + j == n - 1:
                in_diagonal += matrix[i][j]
    print(abs(diagonal - in_diagonal))

