import sys

def solution(array):
    land_count = 0

    def bfs(start_x, start_y):
        queue_indices_to_visit = []

        queue_indices_to_visit.append((i, j))
        # print(indices_to_visit)

        while len(queue_indices_to_visit) != 0:
            # 꺼내고
            x, y = queue_indices_to_visit.pop(0)
            # 방문하고
            array[x][y] = 2  # visited
            # 다 넣고.
            queue_indices_to_visit = enqueue_eight_sides(array, queue_indices_to_visit, x, y)
            # print(f"enqueue_eight_sides {x, y} 반환값: {indices_to_visit}")

    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == 1: # land
                land_count += 1

                bfs(i, j)

    return land_count



# i, j 기준 8칸 중 'visited == 1인 것만' enqueue
def enqueue_eight_sides(array, queue, i, j):
    new_queue = queue

    sides = get_valid_eight_sides(i, j, len(array), len(array[0]))
    if sides is None: return queue

    for i, j in sides:
        if array[i][j] == 1 and (i, j) not in queue:
            new_queue.append((i, j))
    return new_queue

# i, j 기준 모든 8칸 탐색, '길이 넘지 않는 선에서' valid 값만 반환(returns eight sides not exceeding each length)
def get_valid_eight_sides(i, j, len_m, len_n):
    directions = [
        (-1,-1),
        (-1, 0),
        (-1,+1),
        (0, -1),
        (0, +1),
        (+1, -1),
        (+1, 0),
        (+1, +1)
     ]

    result = []
    for dx, dy in directions:
        x, y = i+dx, j+dy
        if len_m > x >= 0 and 0 <= y < len_n:
            result.append((x, y))

    return result


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