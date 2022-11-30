########정수를 이어 붙여서 가장 큰 값 만들게 하는 함수 만들기

def solution(num):
    num = list(map(str, num))
    num.sort(key=lambda x: x * 3, reverse=True)
    return str(int(''.join(num)))

print(solution([10,20,30]))