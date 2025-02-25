import sys

# 0: 회문
# 1: 유사회문
# 2: 아님

## 주의(마지막 반례): xyyyyyxy은 1이어야 함.

# 1개만 삭제 가능해야하므로 전체를 통제하는 변수 필요 - 반복문 사용하기. 재귀를 쓰면 parameter로 삭제 가능 여부 넣어야 하는데 추잡
def is_palindrome_two_independent_pointer(string):
    leftPointer = 0
    rightPointer = len(string)-1

    while leftPointer < rightPointer:
        if string[leftPointer] != string[rightPointer]:
            # 둘 중 하나만 하는 게 아니라 둘 다 해보고 둘 중 하나라도 True이면 return 1
            check1 = is_pure_palindrome(string, leftPointer + 1, rightPointer)
            check2 = is_pure_palindrome(string, leftPointer, rightPointer - 1)
            return 1 if check1 or check2 else 2
        leftPointer += 1
        rightPointer -= 1

    return 0

def is_pure_palindrome(s, left, right):
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


# 백준 입력 처리
N = int(sys.stdin.readline().strip())  # 테스트 개수
inputs = [sys.stdin.readline().strip() for _ in range(N)]  # 모든 입력 저장

# 결과 계산 후 한 번에 출력
results = [str(is_palindrome_two_independent_pointer(string)) for string in inputs]
print("\n".join(results))
# for result in results:
#     print(result)