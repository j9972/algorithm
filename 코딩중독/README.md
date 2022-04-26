##코딩중독 (백준)
#Question 10951번 -> 특별한 테스트 케이스 입력, 종료조건 없이 while문을 써서 값 호출하는 방법

1. while True:
   try - except 문 사용 하기

#Question 11721번 -> 특별한 테스트 케이스 입력, 종료조건 없이 while문을 써서 값 호출하는 방법

1. 전체길이가 길떼 10개씩 끊어서 출력한다 등은 for 문의 마지막인수를 생각
   for i in range(0, end+1, 10) ,
   그리고 시작하는 j = i + 10 이런식으로 다음의 수도 생각해주기

#Question 1924 -> 요일 구하기

1. (1년 전체 일수를 구한 값 + 일) % 7 로 요일 구할 수 있음

#Question 2751 -> 테스트 케이스는 주워지지만, 테스트 개수만큼의 수가 주워진다는 말이 있다면 쓰기

1. import sys -> int(sys.stdin.readline())

#Question 11726 -> 나올 수 있는 경우의 수 구하기 -> 바텀업의 대표적인 방식

1. 바텀업 방식으로 d[0] \* 1001 , d[1] = 1, d[2] = 2를 지정하고 시작하면 될거같음

#Question 11652 -> 딕셔너리 최빈값 구하기

1. 딕셔너리의 키, 값 쌍 얻기 - items()

DP문제는 항상 점화식과 규칙을 찾는 것이 중요하다고 생각합니다.
DP에서 0으로 설정하고 숫자를 더해서 최댓값을 정해주는 식으로 하기

#Question 10814 -> 다른 data type을 리스트에 넣는방법

1. 2개의 데이터를 str으로 input()하고, 다른 한개의 데이터 형변환을 해서 list에 넣으면 된다
2. list에 넣을때는 data.append((age, name)) 이런식으로

#Question 10825 -> 여러개 정렬 조건 나열

1. 첫번째 인자 기준 오름차순, 2번째 인자 기준 내림차순 예시
   -> f = sorted(e, key = lambda x : (x[0], -x[1]))

#Question 2156 -> 개미전사랑 비슷한데 최대 2개까지 연속 가능

1.  dp[0] = arr[0]
    dp[1] = arr[0] + arr[1]
    dp[2] = max(arr[0]+arr[2], arr[2]+arr[1], dp[1])

    for i in range(3, n):
    dp[i] = max(dp[i-2] + arr[i], dp[i-3]+arr[i]+arr[i-1], dp[i-1])

#Question 11055 -> 증가 부분 수열 같은것은 dp를 증가하는 부분 수열 합으로 하기

1. dp[i] = max(dp[i], dp[j]+a[i]) 이렁식으로 합하기

#Question 11054 -> 증가 / 감소 되는 부분 팁

1.  a = list(map(int, input().split()))
    re_a = a[::-1] -> 시작과 끝 부분의 대한 리스트를 따로 만들기
