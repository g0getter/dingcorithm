import sys

# 스택 (시간 초과)개선: stack 변수 사용
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
def get_receiver_top_orders_stack(heights):
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

# 백준 입출력 처리
N = int(sys.stdin.readline().strip())  # 탑 개수
heights = list(map(int, sys.stdin.readline().split()))  # 탑 높이 리스트

# 결과 계산
results = get_receiver_top_orders_stack(heights)

# 결과 출력
print(" ".join(map(str, results)))