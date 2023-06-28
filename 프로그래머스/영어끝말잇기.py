def solution(n, words):
    ans = [0,0]
    check = []
    
    turn = 1
    ppl = 0
    
    while len(words) != 0:
        word = words.pop(0)
        
        if word not in check:
            if len(check) == 0:
                check.append(word)        
            else:
                if check[-1][-1] == word[0]:
                    check.append(word)
                else:
                    ppl += 1
                    if ppl == n+1:
                        ppl = 1
                        turn += 1
                    ans = [ppl,turn]
                    break
        else:
            ppl += 1
            if ppl == n+1:
                ppl = 1
                turn += 1
            ans = [ppl,turn]
            break

        ppl += 1
        if ppl == n+1:
            ppl = 1
            turn += 1
            

    return ans