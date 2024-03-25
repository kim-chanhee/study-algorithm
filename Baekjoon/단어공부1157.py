# - 문제
# 알파벳 대소문자로 된 단어가 주어지면, 이단어에서 가장 많이 사용된 알파벳이 무엇인지

# - 입력 
# 첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.

word = input().lower()  # 알파벳 입력 word = mississipi
word_list = list(set(word))  # 알파벳 리스트 word_list = ['m', 'i', 's', 'p']

cnt = []  # 알파벳 갯수 입력할 리스트

for i in word_list:
    count = word.count(i)
    cnt.append(count)

if cnt.count(max(cnt)) >= 2:
    print("?")

else:
    print(word_list[(cnt.index(max(cnt)))].upper())