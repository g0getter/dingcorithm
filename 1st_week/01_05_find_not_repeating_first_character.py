input = "abadabac"

## 1. My solution
## Time Complexity: O(N) (but much simpler! hehe)
def find_not_repeating_first_character(string):
    # 등장한 문자를 넣어 두는 배열을 만들고
    # string 탐색하며 그 배열에 존재하면 remove, 아니면 append
    # 마지막까지 돌았을 때 return 배열의 첫 번째 문자 or 비었다면 _
    appeared_char = []

    for char in string:
        if char in appeared_char:
            appeared_char.remove(char)
        else:
            appeared_char.append(char)
    if len(appeared_char) == 0:
        return "_"
    else:
        return appeared_char[0]




## 2. Solution in a course
## Time Complexity: O(N)
def find_not_repeating_first_character_use_another_func(string):
    # get `find_alphabet_occurrence_array()` result
    # find first element whose value is 1
      # case i) make a new array 'not_repeating_character_array', and (ii) with condition(if char 'in' the new array)
      # case ii) iterate string (my opinion)
    alphabet_occurrence_array = find_alphabet_occurrence_array(string)

    for char in string:
        index = ord(char) - ord('a')
        if alphabet_occurrence_array[index] == 1:
            return char

    return "_"

def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha(): continue
        index = ord(char) - ord('a')
        alphabet_occurrence_array[index] += 1

    return alphabet_occurrence_array


result = find_not_repeating_first_character
# result = find_not_repeating_first_character_use_another_func
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 = _ 현재 풀이 값 =", result("aaaaaaaa"))