# 프로그래머스
# numbers는 주어지는 리스트 값들
def solution(numbers):
    return str(int(''.join(sorted(list(map(str, numbers)), key=lambda x: x*3, reverse=True))))
    # x*3의 의미는 만약에 6, 10, 2  -> 666, 101010, 222
    # str(int()) 를 쓴 이유는 '0000' -> '0' 으로 변경을 위함
# 문자열 비교연산의 경우엔 첫번째 인덱스인 666[0]인 6과 101010[0]인 1과 222[0]인 2를 ascii숫자로 바꿔서 비교합니다.
# #물론 같으면, 다음 인덱스도 비교합니다. 비교한 결과 [6, 2, 10]의 순으로 정렬됩니다
