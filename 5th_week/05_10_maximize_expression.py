from itertools import permutations
import re

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def maximize_expression(expression):
    # 1. LinkedList로 구현(왜냐면, 매번 계산할 때마다 새로 List를 만드는 건 공간도 많이 차지할 뿐더러, 앞에서부터 끝까지 탐색하며 넣는데에 어차피 LinkedList와 동일하게 N시간이 소요됨.
    #  -> 풀이 방식이 더 단순한 LinkedList 사용
    # 2. 연산자 순열을 담은 배열을 돌며, calc 했을 때 가장 절댓값 큰 수 반환
    # <연산자 순열 하나당 계산 흐름_calc>
    # 0. 현재(첫) 연산자에 대해,
    # 1. prev-cur 구조로 탐색. 첫 연산자가 cur이 나올 때까지 탐색
    # 2. <prev><cur><next> 연산
    # 3. 앞, 뒤 다시 연결
    # 4. 끝까지 간 후, 다음 연산자에 대해 0부터 다시 실행
    # 5. 결과 반환

    # OR

    # <calc> (solution2)
    # 배열 그대로 가되, 새 배열 만들되, 원하는 연산자 발견하면 선행피연산자 빼고 넣고, 결과값 넣고, 계산 계속. -> 끝까지
    # -> 존재하는 연산자에 대해 반복(최대 3번)


    # 0. 문자열 -> 배열로 분리
    # 1. 연산자 뽑아서 순열 생성
    set_operators = set()
    list_expression = regular_expression(expression)
    for op in list_expression:
        if op in ["*","-","+"]:
            set_operators.add(op)
    # print(set_operators)

    permutation_operators = permutes_operators(list(set_operators))

    max_result = 0
    for operators in permutation_operators:
        result = calc(operators, list_expression)
        print(f"{operators} -> {result}")
        max_result = max(max_result, abs(result))

    return max_result

# 배열 그대로 가되, 새 배열 만들되, 원하는 연산자 발견하면 선행피연산자 빼고 넣고, 결과값 넣고, 계산 계속. -> 끝까지
# -> 존재하는 연산자에 대해 반복(최대 3번)
def calc(sorted_operators, expression):
    print(sorted_operators)
    print(expression)


    # for operator in sorted_operators:
    #     new_expression = []
    #     start = 0
    #     for i, val in enumerate(expression):
    #         if val == operator:
    #             result = eval(f"{expression[i-1]}{val}{expression[i+1]}")
    #             # 새 배열 생성
    #             new_expression += expression[start:i-1] + [str(result)]
    #             start = i+1+1
    #             print("new_expression",new_expression)
    # new_expression = []
    for operator in sorted_operators:
        new_expression = []
        start = 0
        for i, val in enumerate(expression):

            if val == operator:
                print("expression", expression)
                result = eval(f"{expression[i-1]}{val}{expression[i+1]}")
                # 새 배열 생성
                new_expression += expression[start:i-1] + [str(result)]
                start = i+1+1
                print("new_expression",new_expression)

        # 초기화
        new_expression += expression[start:]
        expression = new_expression
    ### ('-', '*') 일 때 ['50', '*', '3', '*', '2'] 에서  ['150', '*', '2']으로 만들기 힘들어서 stop..
    ### (150을 넣은 후, *를 만났을 때 3을 기준으로 계산하게 됨. 끝까지 다 넣고 다시 *에 대해 실행하기엔 이미 *의 차례(loop)가 끝난 상태ㅠ 아아악!!!

    return int(new_expression[0])

# 순열 사용
def permutes_operators(operators):
    return list(permutations(operators))


# 정규표현식 사용 (string -> 연산자, 숫자(피연산자) 포함된 배열 반환)
def regular_expression(string):
    # return re.split('[^0-9]', string)
    return re.split('([^0-9])', string) # 매칭된 패턴(연산자)도 포함하기 위해 () 사용


# print("정답 = 60420 / 현재 풀이 값 = ", maximize_expression("100-200*300-500+20"))
print("정답 = 300 / 현재 풀이 값 = ", maximize_expression("50*6-3*2"))