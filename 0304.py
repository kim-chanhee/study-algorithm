# year = int(input())

# if ((year%4==0) and (year%100!=0)) or (year%400==0) :
#     print('1')
# else:
#     print('0')

#=-====================
n = int(input())

nums_pileup = 1  # 벌집의 개수, 1개부터 시작
cnt = 1

while n > nums_pileup :
    nums_pileup += 6 * cnt  # 벌집이 6의 배수로 증가
    cnt += 1
print(cnt)