from itertools import permutations
import re

def solution(expression):
    # 배열 복사한 새로운 배열에서, 연산 후 길이 줄이고 이번 Loop 종료 -> 해당 연산자 존재하지 않을 때까지 반복 -> 모든 연산자에 대해 반복
    # -> 존재하는 연산자에 대해 반복(최대 3번)

    # 0. 문자열 -> 배열로 분리
    # 1. 연산자 뽑아서 순열 생성
    set_operators = set()
    list_expression = regular_expression(expression)
    for op in list_expression:
        if op in ["*","-","+"]:
            set_operators.add(op)

    permutation_operators = permutes_operators(list(set_operators))

    max_result = 0
    for operators in permutation_operators:
        result = calc(operators, list_expression)
        print(f"{operators} -> {result}")
        max_result = max(max_result, abs(result))

    return max_result

# 배열 복사한 새로운 배열에서, 연산 후 길이 줄이고 이번 Loop 종료 -> 해당 연산자 존재하지 않을 때까지 반복 -> 모든 연산자에 대해 반복
# -> 존재하는 연산자에 대해 반복(최대 3번)
def calc(sorted_operators, expression):
    print(sorted_operators)
    print(expression)
    current_expression = expression

    for operator in sorted_operators:
        while operator in current_expression: ## !!!!!. 이번 연산자가 더 이상 없으면 다음 연산자로 넘어가도록.
            i = current_expression.index(operator)
            result = eval(f"{current_expression[i - 1]}{operator}{current_expression[i + 1]}")
            current_expression = current_expression[:i-1] + [str(result)] + current_expression[i+2:]

    return int(current_expression[0])

# 순열 사용
def permutes_operators(operators):
    return list(permutations(operators))


# 정규표현식 사용 (string -> 연산자, 숫자(피연산자) 포함된 배열 반환)
def regular_expression(string):
    return re.split('([^0-9])', string) # 매칭된 패턴(연산자)도 포함하기 위해 () 사용

