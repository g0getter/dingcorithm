import sys


def find_max_num(array):
    # 이 부분을 채워보세요!
    # return max(array)
    max_value = array[0]
    max_index = 0  # 0-based index

    for i, num in enumerate(array):
        if num > max_value:
            max_value = num
            max_index = i  # 인덱스 업데이트
    return max_value, max_index + 1  # 1-based index 반환

# 9개의 정수를 입력받음
numbers = [int(sys.stdin.readline().strip()) for _ in range(9)]

# 최댓값과 위치 찾기
max_value, max_position = find_max_num(numbers)

# 출력 (각 줄에 하나씩)
print(max_value)
print(max_position)