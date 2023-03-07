# #------------------- 단어길이 재기
# word = input()
# word_lst = list(word)
# print(len(word_lst))


# #--------------- 숫자의 합
# n = input()
# N = input()
# total = 0

# #1
# for i in N :
#     total += int(i)

# print(total)

# #2
# for i in range(N):
#     total += int(N[i])
# print(total)


# #--------------------그대로 출력하기
# import sys

# a = [sys.stdin.readline().strip() for _ in range(4)]
# print(a)

# a = input(end = '')
# print(a)

# #------------------------ 문자열 반복
n = int(input())

for _ in range(n):
    cnt, word = input().split()

    for x in word:
        print(x*int(cnt), end='')
    print() # 줄넘김



