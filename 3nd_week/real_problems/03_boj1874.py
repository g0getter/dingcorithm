import sys

# 1. 넣을 수 <= 뽑을 수(sequence) -> 뽑을 수 나올 때까지 push, +1
# 2. 넣을 수 > 뽑을 수 -> pop. -> 같으면 계속 진행(다음 뽑을 수 받아옴)
#                           -> 다르면 return No
def stack_sequence(sequence):
    num_to_add_next = 1 # 넣을 수
    stack = []
    result = []

    for num in sequence:
        if num_to_add_next <= num:
            while num_to_add_next <= num:
                stack.append(num_to_add_next)
                result.append("+")
                num_to_add_next += 1
            # 끝나면 pop
            stack.pop()
            result.append("-")
        else:
            # pop 해서 같은지 확인
            # if stack and stack[-1] == num:
            #     stack.pop()
            if len(stack) > 0 and stack.pop() == num:
                result.append("-")
                continue
            else:
                return ["NO"]

    # true - return +, - sequence splited by \n
    return result

# n = 8
# sequence = [4, 3, 6, 8, 7, 5, 2, 1]
# sequence = [1,2,5,3,4]
# print(stack_sequence(sequence))

# 백준 입출력 처리
n = int(sys.stdin.readline().strip())  # 수열의 길이
sequence = [int(sys.stdin.readline().strip()) for _ in range(n)]  # 입력 받은 수열 리스트

# 결과 출력
print("\n".join(stack_sequence(sequence)))
