import sys
from collections import deque

def solution(array):
    land_count = 0
    
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == 1: # land
                land_count += 1

                dfs(i, j)

    return land_count

def dfs(start_x, start_y):
    directions = [
        (-1, -1),
        (-1, 0),
        (-1, +1),
        (0, -1),
        (0, +1),
        (+1, -1),
        (+1, 0),
        (+1, +1)
    ]

    stack_indices_to_visit = []

    stack_indices_to_visit.append((start_x, start_y))

    while len(stack_indices_to_visit) != 0:
        # 꺼내고
        x, y = stack_indices_to_visit.pop() # 속도 O(1)
        if array[x][y] == 2:  # 중복 방지 - 이미 방문한 경우 스킵
            continue
        # 방문하고
        array[x][y] = 2  # visited

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            # 범위 안에 있고 방문 안 한 land이면
            if 0 <= nx < len(array) and 0 <= ny < len(array[0]) and array[nx][ny] == 1:
                # 차례대로 모두 넣음
                stack_indices_to_visit.append((nx, ny))
                # break # 아니고 일단 같은 레벨은 다 넣어야하므로 기다려줌!
string = """
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
"""

# 함수만 테스트
# array = [list(map(int, line.split())) for line in string.strip().split("\n")]
# print(solution(array))

# 백준 입출력
def readIslandData():
    m, n = map(int, sys.stdin.readline().split())
    if m == 0 and n == 0:
        return None, None, None  # 종료 조건

    array = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    return m, n, array


# 사용 예시
if __name__ == "__main__":
    while True:
        m, n, array = readIslandData()
        if m is None:
            break
        print(solution(array))