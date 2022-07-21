# 입력값은 0혹은 1로만 받는다
data = input()

# 0 <-> 1로 바뀔때마다 count
zeroCount = 0
oneCount = 0

# 첫번째 데이터를 지정
if data[0] == '1':  # string 형식으로 처음에 데이터를 입력받음
    zeroCount += 1
else:
    oneCount += 1

# 2번째 데이터부터 체크
for i in range(len(data)-1):
    # 데이터의 앞뒤가 다른지 체크 ( 2번째 부터 체크 하고 뒤의 데이터와 비교하기에 range범위에 -1을 해줘야한다. )
    if data[i] != data[i+1]:
        if data[i+1] == '1':
            # 1 -> 0으로 바꾸기 때문에 zeroCount 증가
            zeroCount += 1
        else:
            # 0 -> 1으로 바꾸기 때문에 oneCount 증가
            oneCount += 1
print(min(zeroCount, oneCount))
