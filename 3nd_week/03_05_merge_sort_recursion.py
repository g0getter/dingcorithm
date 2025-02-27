# MergeSort(0, N) = Merge(MergeSort(0, N/2) + MergeSort(N/2, N))

# 무작위 배열 array를 정렬해서 반환
def merge_sort(array):
    while len(array) < 2: return array
    # 2개로 쪼개고 그 둘을 합치는 `merge(,)`를 호출

    halfIndex = len(array) // 2

    # 아래 만으로는 불충분. 그냥 단순히 끊기만 했으므로.
    # return merge(array[:halfIndex], array[halfIndex:])
    left_half = merge_sort(array[:halfIndex])
    right_half = merge_sort(array[halfIndex:])
    return merge(left_half, right_half)

def merge(array1, array2):
    # 1. 포인터 2개, 각각 0부터 시작
    # 2. 비교 후 삽입하게 된 포인터는 +1
    # 3. 한 쪽이 끝나면 다른 쪽 원소 나머지 갖다붙임
    pointer1 = 0
    pointer2 = 0
    merged = []

    while pointer1 < len(array1) and pointer2 < len(array2):
        if array1[pointer1] < array2[pointer2]:
            merged.append(array1[pointer1])
            pointer1 += 1
        else:
            merged.append(array2[pointer2])
            pointer2 += 1

    if pointer1 == len(array1):
        merged += array2[pointer2:]
    else:
        merged += array1[pointer1:]

    return merged

array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]
print(merge_sort(array_a+array_b))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!

print("정답 = [-7, -1, 5, 6, 9, 10, 11, 40] / 현재 풀이 값 = ", merge_sort([11, -1, 9, 40, 5, 6, 10, -7]))
print("정답 = [-1, 2, 3, 5, 10, 40, 78, 100] / 현재 풀이 값 = ", merge_sort([-1,2,3,5,40, 10,78,100]))
print("정답 = [-1, -1, 0, 1, 6, 9, 10] / 현재 풀이 값 = ", merge_sort([-1,-1,0, 1, 6, 9, 10]))