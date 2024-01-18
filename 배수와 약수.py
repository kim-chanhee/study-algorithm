for i in range(4):
  a, b = map(int, input('숫자를 입력하시요 : ').split())
  if a==0 and b==0:
        break
  
  if b%a==0 :
    print('factor')
  elif a%b==0:
    print('multiple')
  else :
    print('neiter')
