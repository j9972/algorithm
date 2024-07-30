import sys

n = int(input())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

def find_points(x,y):
    one_sec, two_sec, third_sec, fourth_sec = 0,0,0,0

    for a, b in arr:
        if a == x or b == y:
            return sys.maxsize
        
        if x > a and y < b:
            one_sec += 1
        elif x > a and y > b:
            two_sec += 1
        elif x < a and y < b:
            third_sec += 1
        elif x < a and y > b:
            fourth_sec += 1
    
    return max(one_sec, two_sec, third_sec, fourth_sec)



temp = []

for x in range(101):
    for y in range(101):
        temp.append(find_points(x,y))
print(min(temp))