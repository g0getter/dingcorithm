import sys

# 1. 양쪽 끝 확인 -> 같 -> 계속
#              -> 달 -> 삭제 시(왼 삭 OR 오른 삭) 가능? ==> 삭제 허용 X 함수 필요. 둘의 결과 다 받아서 OR 연산해야하므로.
# -> is_pure_palindrome(string)

def is_palindrome(string):
    for i in range(len(string)//2):
        # print(string[i], string[-i-1])
        if string[i] == string[-i-1]:
            continue
        else:
            # i = 0 일 때 string[1:0]이 되는 것을 방지하기 위해 len(string)을 앞에 넣음.
            if is_pure_palindrome(string[i+1:len(string)-i]) or is_pure_palindrome(string[i:-i-1]):
                return 1
            return 2

    return 0

def is_pure_palindrome(string):
    for i in range(len(string)//2):
        if string[i] != string[-i-1]: return False
    return True

# 백준 입력 처리
N = int(sys.stdin.readline().strip())  # 테스트 개수
inputs = [sys.stdin.readline().strip() for _ in range(N)]  # 모든 입력 저장

# 결과 계산 후 한 번에 출력
results = [str(is_palindrome(string)) for string in inputs]
print("\n".join(results))