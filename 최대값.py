# table =[list(map(int, input().split())) for _ in range(9)]
# max_value = table[0][0] # 최대값
# max_position = (0,0)

# # 행렬 순회하며 최대값과 위치 찾기
# for i in range(9):
#     for j in range(9):
#         if table[i][j] > max_value:
#             max_value = table[i][j]
#             max_position = i, j
    
# print(max_value)
# print(max_position)

table = [list(map(int, input().split())) for _ in range(9)]

max_num = 0
max_row, max_col = 0, 0
for row in range(9):
    for col in range(9):
        if max_num <= table[row][col]:
            max_row = row + 1
            max_col = col + 1
            max_num = table[row][col]

print(max_num)
print(max_row, max_col)
