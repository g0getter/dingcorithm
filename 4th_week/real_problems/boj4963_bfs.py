import sys

def solution(array):
    land_count = 0
    indices_to_visit = []
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == 1: # land
                land_count += 1
                indices_to_visit.append((i,j))
                # print(indices_to_visit)

                while len(indices_to_visit) != 0:
                    # 꺼내고
                    x, y = indices_to_visit.pop(0)
                    # 방문하고
                    array[x][y] = 2  # visited
                    # 다 넣고.
                    indices_to_visit = enqueue_eight_sides(array, indices_to_visit, x, y)
                    # print(f"enqueue_eight_sides {x, y} 반환값: {indices_to_visit}")

    return land_count

# i, j 기준 8칸 탐색, visited==1 이면 enqueue
def enqueue_eight_sides(array, indices_to_visit, i, j):
    new_indices_to_visit = indices_to_visit

    sides = get_valid_eight_sides(i,j, len(array), len(array[0]))
    if sides is None: return indices_to_visit

    for i, j in sides:
        if array[i][j] == 1 and (i, j) not in indices_to_visit:
            new_indices_to_visit.append((i, j))
    return new_indices_to_visit

# returns eight sides not exceeding each length
def get_valid_eight_sides(i, j, len_m, len_n):
    dd = [
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
    for d in dd:
        x = i+d[0]
        y = j+d[1]
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