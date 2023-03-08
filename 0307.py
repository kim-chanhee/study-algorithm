# 피보나치 수열

def fib(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
    
n = int(input())
print(fib(n))

#Q? 메모리제이션 활용해서 다시 풀어보기
#-------------
# 팩토리얼

# def fac(n):
#     if(n>1):
#         return n*fac(n-1)
#     else:
#         return 1

# n = int(input("숫자를 입력하시요 :"))
# print(fac(n))
