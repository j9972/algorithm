1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
def solution(skill, skill_trees):
    cnt = 0
    ans = []

    for tree in skill_trees:
        str1 = ""
        for data in tree:
            if data in skill:
                str1 += data
            else:
                continue
        ans.append(str1)

    for i in ans:
        if skill[:len(i)] == i:
            cnt += 1
        else:
            continue
    return cnt