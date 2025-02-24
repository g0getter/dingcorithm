# ✅https://school.programmers.co.kr/learn/courses/30/lessons/120812 최빈값 구하기

from subprocess import check_output
from typing import OrderedDict

# TODO: modify and develop
# Solution1
def find_max_occurred_alphabet_dictionary(string):
    # 자료구조에 존재하면 새로 추가하고 count를 1 증가. 아니면 그냥 1 증가
    # tuple인지 dictionary 의 key/value를 0, 1로 접근해야해서 별로.
    alphabet_count = {}
    for char in string:
        if not char.isalpha(): continue

        if char in alphabet_count:
            alphabet_count[char] += 1
        else:
            alphabet_count[char] = 1

    max_pair = list(alphabet_count.items())[0]

    for pair in alphabet_count.items():
        if pair[1] > max_pair[1]: # pair.value > max_pair.value
            max_pair = pair
        elif pair[1] == max_pair[1] and ord(pair[0]) < ord(max_pair[0]):
            max_pair = pair

    return max_pair[0] # max_pair.value

def find_alphabet_occurrence_array(array):
    number_occurrence_array = [0] * 1000

    for number in array:
        number_occurrence_array[number] += 1

    return number_occurrence_array

# Solution2
def find_max_occurred_alphabet_static_array(array):

    # 1. fill `count_list`
    count_list = find_alphabet_occurrence_array(array)
    print(count_list)
    # 2. find the maximum occurred element
    max_occurred_number = 0
    has_multiple_maxes = False
    for i in range(1, len(count_list)):
    # or
    # for i in range(len(count_list)):
        if count_list[i] > count_list[max_occurred_number]:
            max_occurred_number = i
            has_multiple_maxes = False
        elif count_list[i] == count_list[max_occurred_number]:
            has_multiple_maxes = True

    if has_multiple_maxes:
        return -1
    else:
        return max_occurred_number

result = find_max_occurred_alphabet_static_array
# print("정답 = 3 현재 풀이 값 =", result([1, 2, 3, 3, 3, 4]))
# print("정답 = -1 현재 풀이 값 =", result([1, 2]))
# print("정답 = 1 현재 풀이 값 =", result([11, 1, 1]))
print("정답 = 0 현재 풀이 값 =", result([0, 1, 0]))
# print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
# print("정답 = b 현재 풀이 값 =", result("best of best youtube"))

