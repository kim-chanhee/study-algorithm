# 0부터 9999까지 8을 포함하지 않는 수는 총 몇개일까?
# 8, 108, 888, 9998 등은 8을 포함하고 있는 수입니다. 111, 299, 4 등과 같은 수는 8을 포함하지 않는 수 입니다.

# count =0
# for i in range(0,1000):
#     if "8" in str(i):
#         count+=1
#         print("8을 포함하는 숫자의 개수는{}개입니다.".format(count))
 

count=0
for i in range(10000):
    if "8" in str(i):
        count+=1
print(10000-count)


a=[]
for i in range(10000):
    if '8' not in str(i):
        a.append(i)
print(len(a))





