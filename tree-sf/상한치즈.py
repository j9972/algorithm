n,m,d,s = map(int,input().split())

# 몇번째 사람, 몇번째 치즈, 언제 먹었어
eating_history = [
    list(map(int,input().split())) 
    for _ in range(d)
]

eating_history.sort(key = lambda x : x[2]) # 먹은 순서대로 정렬

# 몇번째 사람, 언제 아팠는지
sick_history = [
    list(map(int,input().split()))
    for _ in range(s)
]

sick_history.sort(key = lambda x : x[1]) # 아파지기 시작한 순서대로 정렬

cheese = dict()

for i in range(m):
    cheese[i] = []

for sp,st in sick_history:
    for ep,ec,et in eating_history:
        if ep == sp and et < st:
            cheese[ec-1].append(ep)

max_val = 0
for i in range(m):
    if len(set(cheese[i])) == s:
        sick_person = [0] * n
        
        for ep, ec, et in eating_history:
            if ec == i+1:
                sick_person[ep-1] = 1

        max_val = max(max_val, sum(sick_person))
print(max_val)