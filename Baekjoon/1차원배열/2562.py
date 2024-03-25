# 9개의 서로 다른 자연수가 주어질때, 이들 중 최대값을 찾고
# 그 최댓값이 몇 번째 수인지를 구하는 프로그램
# 예를 들어, 서로 다른 9개의 자연수 
# 3,29,38,12,57,74.40.85.61
# 이 주어지면, 이들 중 최댓값은 85이고 이 값은 8번째 수이다.

# X = list(map(int, input().split()))
# max = X[0]

# for i in X:
#     if i > max:
#         max = i

# print(max)
# print(X.index(max)+1)
#===============
num_list = []
for i in range(9):
    num_list.append(int(input()))

print(max(num_list))
print(num_list.index(max(num_list))+1)