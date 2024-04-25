'''
[1]
[1,3]
[1,3,5]
[1,3,5,4]
[1,3,5] (0을 불렀기 때문에 최근의 수를 지운다)
[1,3] (0을 불렀기 때문에 그 다음 최근의 수를 지운다)
[1,3,7]
[1,3] (0을 불렀기 때문에 최근의 수를 지운다)
[1] (0을 불렀기 때문에 그 다음 최근의 수를 지운다)
[1,6]
합은 7이다.
'''
# list = []
# a = int(input())
# for i in range(a):
#     b = int(input())
#     if b==0 and list:
#         list.pop()
#     else:
#         list.append(b)
#     print(list)

# total_sum = sum(list)
# print(f'list sum: {total_sum}')

numbers = []  # 'list' 대신 'numbers' 사용
a = int(input())
for i in range(a):
    b = int(input())
    if b == 0 and numbers:
        numbers.pop()
    else:
        numbers.append(b)
# 반복문 동안의 중간 상태 출력을 제거하고, 최종 합계만 출력합니다.
total_sum = sum(numbers)
print(f'{total_sum}')

# numbers = []  # 숫자를 저장할 빈 리스트
# a = int(input("입력할 숫자의 개수를 입력하세요: "))

# for i in range(a):
#     b = int(input("숫자 입력 (0을 입력하면 마지막 숫자 제거): "))
#     if b == 0 and numbers:  # 입력한 숫자가 0이고, 리스트에 요소가 있을 때
#         numbers.pop()  # 리스트의 마지막 요소 제거
#     else:
#         numbers.append(b)  # 리스트에 숫자 추가
#     print(numbers)  # 현재 리스트 상태 출력