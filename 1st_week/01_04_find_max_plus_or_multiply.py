def find_max_plus_or_multiply(array):
    # 0 혹은 1과의 연산이라면 더하고, 아니라면 곱함
    result = 0
    for num in array:
        if num <= 1 or result <= 1:
            result += num
        else:
            result *= num
    return result

result = find_max_plus_or_multiply

print("정답 = 728 현재 풀이 값 =", result([0,3,5,6,1,2,4]))
print("정답 = 8820 현재 풀이 값 =", result([3,2,1,5,9,7,4]))
print("정답 = 270 현재 풀이 값 =", result([1,1,1,3,3,2,5]))