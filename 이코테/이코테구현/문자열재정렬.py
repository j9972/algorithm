# 문자열에서 숫자와 문자 구분하는데 있어서 좋음
import sys
import re
input = sys.stdin.readline

s = input()

# 문자열에서 숫자랑 문자만 구분해서 별도로 리스트 만들기
numbers = re.findall('\d', s)
alphas = re.findall('[A-Z]', s)

# sort가 아닌 sorted를 써야한다
# 문자형식으로 되어 있는 숫자를 정수형으로 바꿈
number = list(map(int, numbers))
alphas = sorted(alphas)

# alphas 리스트에 number 추가
alphas.append(str(sum(number)))


# 리스트를 문자열로 합치는 방법
print(''.join(s for s in alphas))


# 문자열 재정렬
input = sys.stdin.readline

n = input()
str_list = []

num = 0

for i in n:
    if i.isdigit():
        num += int(i)
    else:
        str_list.append(i)

str_list.sort()
str_list.append(num)
res = ''.join(str(s) for s in str_list)
print(res)
