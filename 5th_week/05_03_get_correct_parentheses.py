# from collections import deque # 큐 사용 안 함

# 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
# 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다.
# 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다.
#   3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.
# 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.
#   4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다.
#   4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
#   4-3. ')'를 다시 붙입니다.
#   4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
#   4-5. 생성된 문자열을 반환합니다.

def get_correct_parentheses(balanced_parentheses_string):
    if balanced_parentheses_string == "": return ""

    # 2. 분리
    u, v = separate_to_u_v(balanced_parentheses_string)

    # 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다.
    #   3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.
    if is_correct_parenthesis(u): # 3
        result_v = get_correct_parentheses(v)
        return u + result_v

    # 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.
    #   4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다.
    #   4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
    #   4-3. ')'를 다시 붙입니다.
    #   4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
    #   4-5. 생성된 문자열을 반환합니다.
    else:  # 4
        result = "(" + get_correct_parentheses(v) + ")"
        new_u = u[1:-1]  # TODO: 짧을 경우 정상적으로 동작하는지 확인
        # new_u = new_u[::-1] # WRONG: 단순히 순서 바꾸는 게 아님
        new_u = reverse_parentheses(new_u)
        result += new_u
        return result

def separate_to_u_v(string):
    # stack = [balanced_parentheses_string[0]] # 순서가 중요하지 않아서 stack 대신 정수 변수 사용(음수로 표현)
    u_last_index = 0
    balanced_count = 1 if string[0] == "(" else -1
    for i in range(1, len(string)):
        if string[i] == "(":
            balanced_count += 1
        else:  # ")"
            balanced_count -= 1
        if balanced_count == 0:
            u_last_index = i
            break

    u = string[:u_last_index + 1]
    v = string[u_last_index + 1:]

    return u, v

def is_correct_parenthesis(string):
    stack = []

    for char in string:
        if char == "(":
            stack.append(char)
        else:
            if stack:
                stack.pop()
            else:
                return False
    return len(stack) == 0


def reverse_parentheses(string):
    result = ""

    for char in string:
        if char == "(":
            result += ")"
        else:
            result += "("

    return result


print("정답 = ()(())()/ 현재 풀이 값 = ", get_correct_parentheses("()))((()"))
print("정답 = (((()))) / 현재 풀이 값 = ", get_correct_parentheses(")()()()("))
print("정답 = ()()() / 현재 풀이 값 = ", get_correct_parentheses("()()()"))
print("정답 = ((((()())))) / 현재 풀이 값 = ", get_correct_parentheses(')()()()(())('))