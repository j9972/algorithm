def solution(arr1, arr2):
    n = len(arr1)
    m = len(arr2[0])
    b = len(arr2)
    
    ans = [[0]*(m) for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            for k in range(b):
                ans[i][j] += arr1[i][k] * arr2[k][j]
    
    return ans