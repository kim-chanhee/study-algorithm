# a = list(str, range(10))
# print(a)

# 0228 백준 문제
# 첫째 줄에 정수의 개수 N(1 ≤ N ≤ 100)이 주어진다. 둘째 줄에는 정수가 공백으로 구분되어져있다. 셋째 줄에는 찾으려고 하는 정수 v가 주어진다. 입력으로 주어지는 정수와 v는 -100보다 크거나 같으며, 100보다 작거나 같다.
# a = int(input())
# a_list = list(map(int, input().split()))
# b = int(input())

# print(a_list.count(b))


# 정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오
# A, B =  map(int, input().split())

# a_list = list(map(int, input().split()))

# for i in range(A):
#     if a_list[i] < B:
#         print(a_list[i], end = " ")

# N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.
# N = int(input())
# n_list = list(map(int , input().split()))

# max_n_list = n_list[0]
# min_n_list = n_list[0]

# for i in range(0,N):
#     if int(n_list[i]) > max_n_list:
#         max_n_list = n_list[i] 

#     if int(n_list[i]) < min_n_list: 
#         min_n_list = n_list[i]
# print(max_n_list, min_n_list)
#-------------------------
n = int(input())
nums = list(map(int, input().split()))
max_num = nums[0]
min_num = nums[0]
for i in nums:
    if i > max_num:
        max_num = i
    elif i < min_num:
        min_num = i
print(min_num, max_num)

