from itertools import permutations
import re

## ('-', '*') 일 때 ['50', '*', '3', '*', '2'] 에서  ['150', '*', '2']으로 만들기 힘들어서 stop..
## (150을 넣은 후, *를 만났을 때 3을 기준으로 계산하게 됨. 끝까지 다 넣고 다시 *에 대해 실행하기엔 이미 *의 차례(loop)가 끝난 상태ㅠㅠ
# 수정 주요 포인트 #
# 1. 이미 *의 차례가 끝나지 않도록 있는 동안 계속 실행하기.
# 2. new_expression에 처음부터 넣고 그대로 그것만 조작하기.(!!!!!) -> 머리가 꼬인 주요 원인. -> 배열이 변화하는 모습을 단계별로 직접 써보고 이게 적절한/구현이 편한 로직인지 확인.
# e.g. 처음엔 그냥 expression 탐색하다가 new_expression 만든 후부터는 new_expression 탐색? 말이 안됨.
# -> 처음부터 new_expression을 사용해야하고, 그러므로 처음부터 복사해둬야 함. -> 점차 줄여가는 방식으로 풀기.
# ['50', '*', '6', '-', '3', '*', '2']
# ['300', '-', '3', '*', '2']
# ['300', '-', '6'] ...
### 3. 하나 연산하고 나면 일단 차례 끝내서, 다음 연산자가 업데이트된 current_expression으로 연산하도록 조치(for + break)
### (아니면 업데이트 덜 돼서 다음에 나오는 동일 연산자는 이전 index 기준으로 연산하게 됨)
### => index 뽑을 때 Loop 돌지 말고 expression.index(operator)로 index 뽑으면 간단하게 조치 가능

def maximize_expression(expression):
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
    # return re.split('[^0-9]', string)
    return re.split('([^0-9])', string) # 매칭된 패턴(연산자)도 포함하기 위해 () 사용


print("정답 = 60420 / 현재 풀이 값 = ", maximize_expression("100-200*300-500+20"))
print("정답 = 300 / 현재 풀이 값 = ", maximize_expression("50*6-3*2"))