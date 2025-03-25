def solution(balanced_parentheses_string):
    if balanced_parentheses_string == "": return ""

    # 2. 분리
    # stack = [balanced_parentheses_string[0]]
    u_last_index = 0
    balanced_count = 1 if balanced_parentheses_string[0] == "(" else -1
    for i in range(1, len(balanced_parentheses_string)):
        if balanced_parentheses_string[i] == "(":
            balanced_count += 1
        else:  # ")"
            balanced_count -= 1
        if balanced_count == 0:
            u_last_index = i
            break

    u = balanced_parentheses_string[:u_last_index + 1]
    v = balanced_parentheses_string[u_last_index + 1:]

    if is_correct_parenthesis(u):  # 3
        result_v = solution(v)
        return u + result_v
    else:  # 4
        result = "(" + solution(v) + ")"
        new_u = u[1:-1]  # TODO: 짧을 경우 정상적으로 동작하는지 확인
        # new_u = new_u[::-1] # WRONG: 단순히 순서 바꾸는 게 아님
        new_u = reverse_parentheses(new_u)
        result += new_u
        return result


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

print("정답 = (()())()/ 현재 풀이 값 = ", solution("(()())()"))
print("정답 = ()/ 현재 풀이 값 = ", solution(")("))
print("정답 = ()(())()/ 현재 풀이 값 = ", solution("()))((()"))

print("정답 = (((()))) / 현재 풀이 값 = ", solution(")()()()("))
print("정답 = ((((()())))) / 현재 풀이 값 = ", solution(')()()()(())('))
