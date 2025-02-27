input = [4, 6, 2, 9, 1]


def insertion_sort(array):
    # 1. 맨 앞 1개부터 정렬된 배열로 봄
    # 2. 정렬된 배열의 다음 것을 삽입했다 가정하고 위치 찾기
    #     * 위치 찾기: 맨 뒤부터 '붙어 있는 2개씩' 비교하며 오름차순 기조 유지(뒤의 것이 더 작으면 swap)
    n = len(array)
    for inserted_index in range(1, n):
        # array[start_index] 삽입했다 가정, 위치 찾기 시작
        for i in range(inserted_index, 0, -1):
            if array[i] < array[i-1]:
                array[i], array[i-1] = array[i-1], array[i]
            else:
                break

    return array


insertion_sort(input)
print(insertion_sort(input)) # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [4, 5, 7, 7, 8] / 현재 풀이 값 = ",insertion_sort([5,8,4,7,7]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",insertion_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",insertion_sort([100,56,-3,32,44]))