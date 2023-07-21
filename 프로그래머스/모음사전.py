def solution(word):
    vowel = ['A','E','I','O','U']
    words = []

    def dfs(cur_word):
        if len(cur_word) > 0:
            words.append(cur_word)
        if len(cur_word) == 5:
            return 

        for v in vowel:
            dfs(cur_word+v)
    dfs('')

    words.sort()
    return words.index(word) + 1

def solution(word):
    answer = 0
    alpha  = ["A","E","I","O","U",""]
    ans = []
    for i in alpha:
        for j in alpha:
            for k in alpha:
                for l in alpha:
                    for m in alpha:
                        w = i+j+k+l+m
                        if w not in ans: ans.append(w)
    ans.sort()
    answer = ans.index(word)
    return answer