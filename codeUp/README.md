#CODE UP

Question 06. 특수문자 표현 하는 방법

1. print(r" 백슬래시 출력 \ ") -> 백슬래시 출력 \
2. print('"'"!@#$%^&*()'"'')  -> "!@#$%^&\*()'

#Question 15. 두가지 값을 한줄로 출력 하는 방법

1. print( ) 안에서 쉼표(,)를 찍어 순서대로 나열하면, 그 순서대로 스페이스로 분리되어 출력된다.

#Question 26. 10진수를 16진수 소문자로 표현하기

1. a = int(input())
   - print(hex(a)) -> Oxff 이렇게 나옴
   - print('%x' % a) -> ff 이렇게 소문자로만 나옴
   - print('%X' % a) -> FF 이렇게 대문자로만 나옴

#Question 28. 16진수로 입력 받는 방법

1. a = int(input(), 16) 이렇게 2번째 인자에 진수 수를 써주면 된다.

#Question 32. 문자 1개를 입력받고 다음 문자를 출력

1. n = input()
   - m = ord(n) + 1
   - print(chr(m))

#Question 32. 입력받은 n을 2배하기

1. n = int(input())
   - print(n<<1) 이게 2배
   - print(n>>1) 이게 0.5배
   - print(n<<2) 이게 4배
   - print(n>>3) 이게 0.25배

#Question 55. XOR

1. (c and (not d)) or ((not c) and d) 이런식으로 사용

#Question 58. 비트단위(bitwise) 연산자

1. ~n = -n - 1
2. -n = ~n + 1
3. 비트 연산자 and은 & 로 표시 -> a & b ( a,b는 각 비트 혹은 정수 )
4. 비트 연산자 or은 | 로 표시 -> a & b ( a,b는 각 비트 혹은 정수 )
5. 비트 연산자 xor은 ^ 로 표시 -> a & b ( a,b는 각 비트 혹은 정수 )
