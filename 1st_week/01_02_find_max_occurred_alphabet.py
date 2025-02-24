from subprocess import check_output
from typing import OrderedDict

## 1. My solution - 딕셔너리 사용
## Time Complexity: O(N), Space Complexity: O(1)
def find_max_occurred_alphabet_dictionary(string):
    dict_alphabet_count = {}
    # 딕셔너리에 존재하지 않으면 새로 추가하고 count를 1 증가. 아니면 그냥 1 증가
    for char in string:
        if not char.isalpha(): continue # 알파벳 아닌 것 필터링

        if char in dict_alphabet_count:
            dict_alphabet_count[char] += 1
        else:
            dict_alphabet_count[char] = 1

    # 딕셔너리에서 max value 찾기
    max_alphabet, max_count = list(dict_alphabet_count.items())[0]

    for alphabet, count in dict_alphabet_count.items():
        if count > max_count:
            max_alphabet = alphabet
            max_count = count
        elif count == max_count and ord(alphabet) < ord(max_alphabet): # 같다면, 알파벳 순서가 더 앞일 경우 교체
            max_alphabet = alphabet
            max_count = count

    return max_alphabet



## 2. 수업 solution - 알파벳 개수만큼 고정된 배열 사용
## Time Complexity: O(N), Space Complexity: O(1)
def find_max_occurred_alphabet_static_array(string):
    if string is None: return -1

    # alphabet_occurrence_array = [0] * (ord('z')-ord('a')+1) # [0, 0, ..., 0] 26개

    # 1. fill `alphabet_occurrence_array`
    alphabet_occurrence_array = find_alphabet_occurrence_array(string)

    # 2. find the maximum occurred element
    max_index = 0
    for i, count in enumerate(alphabet_occurrence_array):
    # (or) for i in range(len(alphabet_occurrence_array)):
        if count > alphabet_occurrence_array[max_index]:
            max_index = i
    return chr(max_index+ord('a'))


def find_alphabet_occurrence_array(string):
    # index는 a가 0, z가 25인 배열
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha(): continue
        index = ord(char) - ord('a')
        alphabet_occurrence_array[index] += 1

    return alphabet_occurrence_array

result = find_max_occurred_alphabet_static_array
# result = find_max_occurred_alphabet_dictionary
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))