def find_max_num(array):
    # 이 부분을 채워보세요!
    # return max(array)
    max_value = array[0]

    for num in array:
        if num > max_value:
            max_value = num
    return max_value


print("정답 = 6 / 현재 풀이 값 = ", find_max_num([3, 5, 6, 1, 2, 4]))
print("정답 = 6 / 현재 풀이 값 = ", find_max_num([6, 6, 6]))
print("정답 = 1888 / 현재 풀이 값 = ", find_max_num([6, 9, 2, 7, 1888]))