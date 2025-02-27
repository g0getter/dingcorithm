from os import minor

input = [4, 6, 2, 9, 1]


def selection_sort(array):
    n = len(array)
    for done_count in range(n-1):
        min_index = done_count
        print("done_count:", done_count)
        for i in range(done_count, len(array)):
            # find min
            if array[i] < array[min_index]:
                min_index = i

        # swap with the 'first'
        array[min_index], array[done_count] = array[done_count], array[min_index]

    return array


selection_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [1, 2, 4, 6, 9] / 현재 풀이 값 = ",selection_sort([4, 6, 2, 9, 1]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",selection_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",selection_sort([100,56,-3,32,44]))