for _ in range(int(input())):
    arr = []

    n = int(input())

    val = format(n, 'b')
    
    for i in range(len(val)-1, -1, -1):
        if val[i] == '1':
            print(len(val)-1-i, end=' ')
