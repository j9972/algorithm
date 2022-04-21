n = int(input())
suma = 0
for i in range(1, n + 1):
    suma += i
    if suma >= n:
        break
print(suma)
