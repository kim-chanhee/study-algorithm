# 최소, 최대
# N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램 작서

N = int(input())
X = list(map(int, input().split()))
max = X[0]
min = X[0]

for item in X:
    if item > max:
        max = item
    elif item < min:
        min = item

print(min, max)
