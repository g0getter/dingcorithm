def josephus_problem(n, k):
    result_arr = []

    # 1. 순환하는 링크드리스트를 만들고 제거하면 다시 이어 붙이고... -> 이후 k번째를 탐색해서 제거하는데 리스트가 비면 return
    # -> 링크드리스트를 만들고 제거하고 이어붙이고 k번 탐색하는 것 비용 많이 들 것.
    # 2(최종). list의 index로 끝내보기. mod 연산 이용해서.

    array = list(range(1, n+1))
    index = k-1

    while len(array) > 1:
        result_arr.append(array[index])
        array.remove(array[index]) # == array.pop(index)
        # 다음 index 계산: 없어진 자신을 제외해야 하므로 -1, k만큼 가기 위해 +k, 줄어든(!) array의 길이에 맞춰 mod 연산
        index = (index-1 + k) % len(array)

    result_arr.append(array[0])

    print("<", ", ".join(map(str, result_arr)), ">", sep='')


n, k = map(int, input().split())
josephus_problem(n, k)
