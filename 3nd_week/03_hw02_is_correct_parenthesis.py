# '('를 넣는 stack 만들고 ')  만날 때마다 pop. 종료 후 empty이면 return True, 중간에 pop할 것이 없거나 empty 아니면 return False
def is_correct_parenthesis(string):
    stack = []

    for char in string:
        if char == "(":
            stack.append(char)
        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop()

    return len(stack) == 0


print("정답 = True / 현재 풀이 값 = ", is_correct_parenthesis("(())"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis(")"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())))"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("())()"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())"))