finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

# 1. (wrong solution) iteration + 범위 줄이는 게 아닌 단위 줄이는 방식 -> 헷갈리고, 중복 탐색 가능성이 있음
##### 문제: 존재하지 않으면 무한 루프.
# index 범위 벗어날 수도 있음
# Time complexity: 이상적으로는 O(log N)이지만 범위를 절반으로 정확히 나누지 않기 때문에 탐색 효율이 떨어질 가능성이 있음.
# => 연산 단위 대신 범위를 줄이도록 변경.
def is_existing_target_number_binary_iteration(target, array):
    # 이진탐색 binary search: 반씩 쪼개서 탐색
    # 작으면 작은 곳의 중간, 크면 큰 곳의 중간을 다음 index에 넣어서 탐색
    # 재귀를 쓰되, index를 인자로 받는 함수 or iteration

    if len(array) == 0: return False

    calculation_unit = int(len(array) / 2)
    index = calculation_unit

    # iteration
    while array[index] != target:
        print("at:", index, ", value: ", array[index])
        calculation_unit = int(calculation_unit/2)
        if array[index] > target:
            index = index - calculation_unit
        else:
            index = index + calculation_unit
        print(index)

    return target == array[index]
    # -> 했던 것 다시 탐색하는지 아닌지 애매함.
    # -> 범위 정해주는 재귀로 도전!

# 2. recursion + 범위 줄임
def is_existing_target_number_binary_recursion(target, array):
    # 자기 자신 빼고 범위를 재조정하고 싶으므로 lowerbound, upperbound 받는 탐색함수 정의
    if len(array) == 0: return False

    return is_existing_target_number_in(0, len(array), array, target)

# including `lower`, excluding `upper`
# 중간값 반환
def is_existing_target_number_in(lower: int, upper: int, array, target: int):
    index = int((lower + upper) / 2)

    if lower == upper:
        return target == array[lower]

    if array[index] == target:
        return True
    elif array[index] > target:
        return is_existing_target_number_in(lower, index - 1, array, target)
    else:
        return is_existing_target_number_in(index + 1, upper, array, target)

# 3. iteration + 범위 줄임
def is_existing_target_number_binary_iteration_final(target, array):
    if len(array) == 0: return False

    lowerbound = 0
    upperbound = len(array)-1

    while lowerbound < upperbound:
        index = (lowerbound + upperbound) // 2
        if array[index] == target: return True
        elif array[index] > target:
            upperbound = index - 1
        else:
            lowerbound = index + 1

    return array[lowerbound] == target

# result = is_existing_target_number_binary_recursion(finding_target, finding_numbers)
# result = is_existing_target_number_binary_iteration(finding_target, finding_numbers)
result = is_existing_target_number_binary_iteration_final(finding_target, finding_numbers)

print(result)



# CONCLUSION #

## 2(재귀), 3(반복) 비교
# 반복이 나음. 왜냐면,
# 재귀 - 많은 호출이 쌓이면 오버헤드가 발생할 수 있고, Python에서는 재귀 깊이에 제한.(-> RecursionError 발생 가능)
# 매우 큰 배열에 대해 재귀가 많이 호출되면 메모리 상에 스택을 많이 차지해서 스택 오버플로우가 발생 가능

## 내가 기억할(!) 이진 탐색의 기본: 범위 줄여서 upper, lower 같아지면 '탐색 끝난 것'(기든 아니든). 그때 결론 내리면 됨.