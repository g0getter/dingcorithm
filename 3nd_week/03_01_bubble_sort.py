input = [4, 6, 2, 9, 1]


def bubble_sort(array):
    n = len(array)
    
    # done_count: 현재 정렬 완료된 개수. 5개라면 4개가 정렬 완료되면 끝난 것이므로 done_count가 4부턴 할 필요 없음.
    # (유의!) 따라서 done_count는 0부터 len(array)-2까지 들어가면 됨.
    for done_count in range(n-1):
        for i in range(n-done_count-1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i] # swap

    return array



bubble_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [1, 2, 4, 6, 9] / 현재 풀이 값 = ",bubble_sort([4, 6, 2, 9, 1]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",bubble_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",bubble_sort([100,56,-3,32,44]))