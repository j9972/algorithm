import sys

n,l = map(int,input().split())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

ans = 0

def in_range(idx):
    return 0<=idx<n

def compare_height(val, next_val):
    if abs(val - next_val) == 1:
        return True
    else:
        return False

# 2 * n 번 돌리기 ( 순서 뒤집으면 오른, 내림 전부 점검 가능 )
def check_line(temp):

    tmp = [0] * n # 33 22 33 같은 경우처럼 경사로가 겹치는 것을 방지하기 위한 배열
    
    idx = 0
    while idx < n-1:
        if compare_height(temp[idx], temp[idx+1]):
            
            if temp[idx] > temp[idx+1]:
                tmp_val = temp[idx+1]

                if not in_range(idx+l):
                    return False

                for j in range(idx+1, idx+1+l):
                    if tmp[j] == 1: # 경사로가 겹침
                        return False
                    
                    # 경사로를 두기 위해서는 높이가 같아야함
                    if tmp_val != temp[j]: # 높낮이가 같지 않음
                        return False
                    
                    tmp[j] = 1 # 경사로 두기
            
                idx += l # 경사로 둔 만큼 이동

            elif temp[idx] < temp[idx+1]:
                tmp_val = temp[idx]

                if not in_range(idx-l+1):
                    return False
                
                for j in range(idx, idx-l,-1):
                    if tmp[j] == 1: # 경사로가 겹침
                        return False
                    
                    # 경사로를 두기 위해서는 높이가 같아야함
                    if tmp_val != temp[j]: # 높낮이가 같지 않음
                        return False
                    
                    tmp[j] = 1 # 경사로 두기
                
                idx += 1 # 뒤를 체크하는 것이기에 1만 증가

        else:
            if temp[idx] == temp[idx+1]:
                idx += 1
                continue
            else:
                return False
            
    return True

res = []
# 2차원 배열에서 가로줄을 하나의 리스트로 담기
for i in range(n):
    tmp = []
    for j in range(n):
        tmp.append(arr[i][j])
    res.append(tmp)

# 2차원 배열에서 세로줄을 하나의 리스트로 담기
for j in range(n):
    tmp = []
    for i in range(n):
        tmp.append(arr[i][j])
    res.append(tmp)

ans = 0
for i in res:   
    if check_line(i):
        ans += 1
print(ans)