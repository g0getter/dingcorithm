top_heights = [6, 9, 5, 7, 4]

# 1. 반복문, 0으로 초기화 X
# (스택 사용X, 가장 그대로, 생각 없이 구현)
def get_receiver_top_orders_iteration_without_zeros(heights):
    # 스택 안 쓰면 - 가장 그대로, 생각 없이 구현
    results = []

    # 1차 - 반복문, 0으로 초기화X
    for current_i in range(len(heights)):
        for i in range(current_i-1, -1, -1):
            if heights[i] > heights[current_i]:
                results.append(i+1)
                break

        if len(results) <= current_i: # 사실상 ==이라면
            results.append(0)

    return results

# 2. 반복문, 0으로 초기화 O
# (스택 사용X, 가장 그대로, 생각 없이 구현)
def get_receiver_top_orders_iteration_with_zeros(heights):
    results = [0] * len(heights)

    for current_i in range(len(heights)):
        for i in range(current_i-1, -1, -1):
            if heights[i] > heights[current_i]:
                results[current_i] = i+1
                break

    return results

# 3. 스택 사용
# Time complexity: O(N^2)
# (X) 현재 height 올 때까지 stack에 push하며 저장해뒀다가 도착하면 pop하며 대소 확인, 크면 변경 - X!!! push, pop 너무 많이 함.
# (O) mutable heights 활용, current_i로서 heights 자체를 pop하기.
#   맨 끝에서 시작, 본인을 pop하고 나머지는 index로 접근하며 본인보다 큰지 확인. ->  반복
def get_receiver_top_orders_stack(heights):
    results = [0] * len(heights)

    while heights:
        current_height = heights.pop()
        for i in range(len(heights)-1, -1, -1):
            if heights[i] > current_height:
                results[len(heights)] = i+1
                break

    return results

# 4. 스택 개선: stack 변수 사용
# Time complexity: O(N)
# stack: 실질적으로 신호를 받을 수 있는 왼쪽 탑의 후보군.(오름차순으로 정렬되어 있음 - 중간에 오른쪽의 탑보다 작은 게 있으면 어차피 신호를 우측 탑이 미리 받아서 존재가 무의미하므로)
# 자신보다 작은 탑을 미리 제거해서 불필요한 검사를 줄임
# 본인은 왼쪽보다 크든 작든 넣어야 함.
# [구현 과정]
# 1. stack 맨 오른쪽부터 확인
#   존재 O: 나와의 대소 확인
#           - 더 크면: answer에 넣고 나도 push
#           - 더 작으면: pop(무의미하므로)하고 나를 push
#   존재 X: 나를 push
def get_receiver_top_orders(heights):
    stack = []  # [인덱스, 높이]를 저장
    answer = [0] * len(heights)

    for i in range(len(heights)):
        while stack:
            if stack[-1][1] > heights[i]:
                answer[i] = stack[-1][0] + 1 # index+1
                break
            else:
                stack.pop()

        stack.append([i, heights[i]])
    return answer


# print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!
print("정답 = [0, 0, 2, 2, 4] / 현재 풀이 값 = ",get_receiver_top_orders([6,9,5,7,4]))
print("정답 = [0, 0, 0, 3, 3, 3, 6] / 현재 풀이 값 = ",get_receiver_top_orders([3,9,9,3,5,7,2]))
print("정답 = [0, 0, 2, 0, 0, 5, 6] / 현재 풀이 값 = ",get_receiver_top_orders([1,5,3,6,7,6,5]))