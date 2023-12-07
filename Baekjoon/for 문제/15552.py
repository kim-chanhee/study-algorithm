import sys

Case = int(input())

for i in range(Case):
    A,B = map(int, sys.stdin.readline().split())

    print(A+B)