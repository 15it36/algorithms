""" Birthday Cake problem """
if __name__ == '__main__':
    age = int(input())
    candle = list(map(int, input().rstrip().split()))
    candle.sort()
    large_count = candle.count(candle[len(candle) - 1])
    print(large_count)
