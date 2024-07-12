string = input()
boom = input()

b = len(boom)
st = []

for i in string:
    st.append(i)

    if len(st) >= b and ''.join(st[-b:]) == boom:
        for _ in range(b):
            st.pop()

if len(st) == 0:
    print("FRULA")
else:
    print(''.join(st))