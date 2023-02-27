# a = int(input())
# for i in range(1,10):
#     print(a,"*",i,"=",a*i)

#==========
# a = int(input())
# b= int(input())

# print(a+b)
#=========
# plus = list(map(int, input().split()))

# print(plus)\
#=============
# def solution(money):
    
#     m = 0
#     n = 0
    
#     if money % 5500 == 0 :
#         m += 1
    
#     else:
#         m = money//5500
#         n = money%5500
    
#         answer = [m,n]
    
#     return answer
    #==============
# A, B = input().split()	# 입력되는 문자를 input()함수로 입력받고 split()함수로 나누어 A,B 변수에 저장

# print(int(A)+int(B))
#=========
score = int(input("시험 점수를 입력하시요 : "))

if score >= 90:
    print('A')

elif score >= 80:
    print('B')

elif score >= 70:
    print('C')

elif score >= 60:
    print('D')

else:
    print('F')





