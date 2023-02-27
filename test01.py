# 자연수 리스트(홀수와 짝수의 개수가 같음)가 주어집니다.(예외 처리 필요) 이 리스트를 정렬해야 합니다. 순서는 홀-짝-홀-짝-...으로 오게 해야 하며, 홀수는 오름차순 정렬로, 짝수는 내림차순 정렬로 배치해야 합니다.
sample_input = "413265"
odd = [int(x) for x in sample_input if int(x)%2==1]
even = [int(x) for x in sample_input if int(x)%2==0]

sample_output=[]
for i in range(3):
    sample_output.append(sorted(odd)[i])
    sample_output.append(sorted(even, reverse=True)[i])
print(sample_output)
#===================================
from itertools import chain

nums = [4, 1, 3, 2, 6, 5]
even = sorted([x for x in nums if x % 2 == 0], reverse=True)
odd = sorted([x for x in nums if x % 2 == 1])
print(*chain(*zip(odd, even)))