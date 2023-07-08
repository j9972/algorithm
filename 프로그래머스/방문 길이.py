def solution(a):
    x,y = 0,0
    answer = []
    
    for direction in a:
        if (direction == 'U') and (-5<=y<=4 and -5<=x<=5):
            next_x = x
            next_y = y + 1
            if [x,y,next_x,next_y] not in answer:
                answer.append([x,y,next_x,next_y])
                answer.append([next_x,next_y,x,y])

        elif (direction == 'L') and (-5<=y<=5 and -4<=x<=5):
            next_x = x - 1
            next_y = y 
            if [x,y,next_x,next_y] not in answer:
                answer.append([x,y,next_x,next_y])
                answer.append([next_x,next_y,x,y])
                
        elif (direction == 'R') and (-5<=y<=5 and -5<=x<=4):
            next_x = x + 1
            next_y = y 
            if [x,y,next_x,next_y] not in answer:
                answer.append([x,y,next_x,next_y])
                answer.append([next_x,next_y,x,y])
            
        elif (direction == 'D') and (-4<=y<=5 and -5<=x<=5):
            next_x = x 
            next_y = y - 1
            if [x,y,next_x,next_y] not in answer:
                answer.append([x,y,next_x,next_y])
                answer.append([next_x,next_y,x,y])
            
        x = next_x
        y = next_y
            
    return len(answer) // 2