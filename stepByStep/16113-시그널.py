n = int(input())
arr = list(input())

zero = ['#','#','#','#','#','#','.','.','.','#','#','#','#','#','#']
one = ['#','#','#','#','#']
two = ['#','.','#','#','#','#','.','#','.','#','#','#','#','.','#']
three = ['#','.','#','.','#','#','.','#','.','#','#','#','#','#','#']
four = ['#','#','#','.','.','.','.','#','.','.','#','#','#','#','#']
five = ['#','#','#','.','#','#','.','#','.','#','#','.','#','#','#']
six = ['#','#','#','#','#','#','.','#','.','#','#','.','#','#','#']
seven = ['#','.','.','.','.','#','.','.','.','.','#','#','#','#','#']
eight = ['#','#','#','#','#','#','.','#','.','#','#','#','#','#','#']
nine = ['#','#','#','.','#','#','.','#','.','#','#','#','#','#','#']
blank = ['.','.','.','.','.']

number = [
    arr[i * (n//5) : (i+1) * (n//5)]
    for i in range((n + (n//5) - 1) // (n//5))
]

temp, ans = list(), list()

for i in range(n//5):
    for j in range(5):

        temp.append(number[j][i])

        if temp == zero:
            ans.append(0)
            temp= []
        elif temp == one and i < (n//5) - 1:
            if number[j][i+1] == '.':
                ans.append(1)
                temp = []
        elif temp == one and i == (n//5)-1 and j == 4:
            ans.append(1)
            temp = []
        elif temp == two:
            ans.append(2)
            temp = []
        elif temp == three:
            ans.append(3)
            temp = []
        elif temp == four:
            ans.append(4)
            temp = []
        elif temp == five:
            ans.append(5)
            temp = []
        elif temp == six:
            ans.append(6)
            temp = []
        elif temp == seven:
            ans.append(7)
            temp = []
        elif temp == eight:
            ans.append(8)
            temp = []
        elif temp == nine:
            ans.append(9)
            temp = []
        elif temp == blank:
            temp = []
            
for i in ans:
    print(int(i),end="")