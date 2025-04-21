from collections import deque


def is_available_to_take_out_only_red_marble(game_map):
    queue = deque()
    m = len(game_map)
    n = len(game_map[0])

    visited = [[[[False] * n for _ in range(m)] for _ in range(n)] for _ in range(n)]

    # red, blue 초기 위치 찾기
    red_r, red_c, blue_r, blue_c = -1, -1, -1, -1
    for i in range(len(game_map)):
        for j in range(len(game_map[0])):
            if game_map[i][j] == "R":
                red_r, red_c = i, j
            elif game_map[i][j] == "B":
                blue_r, blue_c = i, j
    queue.append((red_r, red_c, blue_r, blue_c, 0)) # 현재 0번 이동했으므로 count = 0

    dr = [0,1,0,-1]
    dc = [1,0,-1,0]

    while queue: # 일단 뽑아서 진행할거라 비어 있는지만 확인. count 확인까지는 X
        red_r, red_c, blue_r, blue_c, count = queue.popleft()
        if count > 10: # 넣을 때는 검사 X. 어차피 10까지만 넣을거니까 더 늘지는 않음.
             continue # 다음 걸로 넘어감 (=사실상 break와 같은 효과_count 같은 것끼리 인접해서 넣으므로)

        # 4 방향 이동시키고 queue에 넣기
        for i in range(len(dr)):
            next_red_r, next_red_c, movement_red = move(red_r, red_c, dr[i], dc[i], game_map)
            # print(red_r, red_c, dr[i], dc[i], "=>", next_red_r, next_red_c)
            next_blue_r, next_blue_c, movement_blue = move(blue_r, blue_c, dr[i], dc[i], game_map)
            # print(blue_r, blue_c, dr[i], dc[i], "=>", next_blue_r, next_blue_c)

            # 확인해서 적절하면 queue에 추가
            # 0. 적절: blue가 구멍에 빠지지 않았으면. (=red가 먼저 들어가든 말든 일단 blue가 빠질 수 있다면 실패!!!)
            if game_map[next_blue_r][next_blue_c] == "O":
                continue # 다음 걸로 넘어감. return False X.
            elif game_map[next_red_r][next_red_c] == "O":
                return True

            # 1. 적절: 둘이 겹치지 않고, 방문한 적이 없으면
            # 겹치면 조정
            if next_red_r == next_blue_r and next_red_c == next_blue_c:
                if movement_red > movement_blue: # 더 많이 움직인 걸 1보 후퇴
                    next_red_r -= dr[i]
                    next_red_c -= dc[i]
                else:
                    next_blue_r -= dr[i]
                    next_blue_c -= dc[i]
            # 방문한 적 없으면 visited 업데이트하고 queue에 추가
            if not visited[next_red_r][next_red_c][next_blue_r][next_blue_c]:
                visited[next_red_r][next_red_c][next_blue_r][next_blue_c] = True
                queue.append((next_red_r, next_red_c, next_blue_r, next_blue_c, count+1))

    return False

# 최대한 끝까지 이동하고, 위치와 움직인 칸 수를 반환
# 최대한 끝까지: 벽 전까지 혹은 구멍까지
def move(r, c, dr, dc, game_map):
    total_movement = 0

    # 현재가 구멍이거나 다음이 벽이면 return
    while game_map[r][c] != "O" and game_map[r+dr][c+dc] != "#":
        total_movement += 1
        r = r + dr
        c = c + dc

    return r, c, total_movement

game_map = [
    ["#", "#", "#", "#", "#"],
    ["#", ".", ".", "B", "#"],
    ["#", ".", "#", ".", "#"],
    ["#", "R", "O", ".", "#"],
    ["#", "#", "#", "#", "#"],
]
print("정답 = True / 현재 풀이 값 = ", is_available_to_take_out_only_red_marble(game_map))


game_map = [
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", ".", "O", ".", ".", ".", ".", "R", "B", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]
]
print("정답 = False / 현재 풀이 값 = ", is_available_to_take_out_only_red_marble(game_map))


game_map = [
["#", "#", "#", "#", "#", "#", "#"],
["#", ".", ".", "R", "#", "B", "#"],
["#", ".", "#", "#", "#", "#", "#"],
["#", ".", ".", ".", ".", ".", "#"],
["#", "#", "#", "#", "#", ".", "#"],
["#", "O", ".", ".", ".", ".", "#"],
["#", "#", "#", "#", "#", "#", "#"]
]
print("정답 = True / 현재 풀이 값 = ", is_available_to_take_out_only_red_marble(game_map))