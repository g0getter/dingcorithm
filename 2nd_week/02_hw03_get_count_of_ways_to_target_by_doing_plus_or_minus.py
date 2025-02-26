numbers = [1, 1, 1, 1, 1]
target_number = 3


# numbers = [1,1,1]
# target_number = 1

# 1(X). (1) 일단 골라서 주어진 숫자 만들기가 가능한지 (2) 나머지 수로 0 만들기 가능한지? - 사용 불가. 더하고 빼야 주어진 숫자가 만들어질 수도 있음.
# e.g. 4,4,4,1 -> 3 만들기.
# 2. brute-force: O(2^n) 소요
# 3(GOOD). 본인을 더한 값을 본인을 제외한 나머지 항목으로 만들 수 있는 '경우의 수' + 본인을 뺀 값을 ~ -> 재귀!(이전 값을 그대로 사용할 수는 없으므로 dp는 아님)
def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target):
    # print("me:",array[0],"array:",array, "target:", target)
    if len(array) == 0: return 0
    if len(array) == 1: return 1 if array[0] == target or array[0] * (-1) == target else 0

    me = array[0]
    # ways_plus + ways_minus
    return (
            get_count_of_ways_to_target_by_doing_plus_or_minus(array[1:], target - me)
            +
            get_count_of_ways_to_target_by_doing_plus_or_minus(array[1:], target + me)
    )


print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number))  # 5를 반환해야 합니다!
