k = 4  # 말의 개수

chess_map = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
start_horse_location_and_directions = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 2, 0],
    [2, 2, 2]
]
# 이 경우는 게임이 끝나지 않아 -1 을 반환해야 합니다!
# 동 서 북 남
# →, ←, ↑, ↓
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

# 1. current_stacked_horse_map 초기화: 현재 맵의 상태. 복잡하니까 방향 없이 말 번호만 놓아보기.
# 2. turn 횟수 추가, 말들을 규칙에 맞게 움직이기 (단, 현재 말들의 위치 집합: horse_location_and_directions. 계속 업데이트하기)
    # 파란색은 범위 out과 같은 경우이므로 파란색과 범위 out 경우를 맨 위의 조건으로 올림
# 3. return 조건(horse 쌓인 개수 4) 추가

def get_game_over_turn_count(horse_count, game_map, horse_location_and_directions):
    n = len(game_map)
    current_stacked_horse_map = [[[] for _ in range(n)] for _ in range(n)]
    #1
    for i, (r, c, d) in enumerate(horse_location_and_directions):
        current_stacked_horse_map[r][c].append(i)

    # printMap(current_stacked_horse_map)

    #2
    turn_count = 1
    while turn_count <= 10:
        print("turn", turn_count)
        printMap(current_stacked_horse_map)
        for horse_num in range(horse_count): # e.g. 0, 1, 2, 3
            r, c, d = horse_location_and_directions[horse_num]
            next_r = r + dr[d]
            next_c = c + dc[d]

            # 무엇을 옮길지 정함
            moving_horse_index_array = []
            for i, horse in enumerate(current_stacked_horse_map[r][c]):
                if horse == horse_num: # 현재 말의 위치 찾기: i
                    moving_horse_index_array = current_stacked_horse_map[r][c][i:]
                    current_stacked_horse_map[r][c] = current_stacked_horse_map[r][c][:i] # 기존 것 비움(제거)
                    break
            print("옮긴 말들:", moving_horse_index_array)



            # 옮기기 - 다음 칸 색깔에 따라

            # 파란색인 경우에는 A번 말의 이동 방향을 반대로 하고 한 칸 이동한다. 방향을 반대로 바꾼 후에 이동하려는 칸이 파란색인 경우에는 이동하지 않고 가만히 있는다.
            # 체스판을 벗어나는 경우에는 파란색과 같은 경우이다.
            if not (0 <= next_r < n and 0 <= next_c < n) or game_map[next_r][next_c] == 2: # 벗어나거나 파란색인 경우
                next_d = reversed_direction(d)
                next_r = r + dr[next_d]
                next_c = c + dc[next_d]

                horse_location_and_directions[horse_num][2] = next_d # ⭐️방향 반대로
                # 바꾼 후에 이동하려는 칸이 벗어나거나 파란색인 경우
                if not (0 <= next_r < n and 0 <= next_c < n) or game_map[next_r][next_c] == 2:
                    # next_r = r
                    # next_c = c
                    continue

                current_stacked_horse_map[next_r][next_c] += moving_horse_index_array
                # for horse in moving_horse_index_array:
                #     # horse_location_and_directions[horse] = [next_r, next_c, next_d]
                #     horse_location_and_directions[horse][0], horse_location_and_directions[horse][1] = next_r, next_c
                # horse_location_and_directions[horse_num] = [next_r, next_c, next_d]

            # 흰색인 경우에는 그 칸으로 이동한다. 이동하려는 칸에 말이 이미 있는 경우에는 가장 위에 A번 말을 올려놓는다.
            elif game_map[next_r][next_c] == 0:
                current_stacked_horse_map[next_r][next_c] += moving_horse_index_array
                # horse_location_and_directions[horse_num] = [next_r, next_c, d]
                # for horse in moving_horse_index_array:
                #     # horse_location_and_directions[horse] = [next_r, next_c, d] # XXXXXX!
                #     horse_location_and_directions[horse][0], horse_location_and_directions[horse][1] = next_r, next_c

            # 빨간색인 경우에는 이동한 후에 A번 말과 그 위에 있는 모든 말의 쌓여있는 순서를 반대로 바꾼다.
            # A, D, F, G가 이동하고, 이동하려는 칸에 말이 E, C, B로 있는 경우에는 E, C, B, G, F, D, A가 된다.
            elif game_map[next_r][next_c] == 1:
                current_stacked_horse_map[next_r][next_c] += reversed(moving_horse_index_array)
                # horse_location_and_directions[horse_num] = [next_r, next_c, d]

                # for horse in moving_horse_index_array:
                #     # horse_location_and_directions[horse] = [next_r, next_c, d] # XXXXXX!
                #     horse_location_and_directions[horse][0], horse_location_and_directions[horse][1] = next_r, next_c

            # 이동: 공통 코드
            for horse in moving_horse_index_array:
                # horse_location_and_directions[horse] = [next_r, next_c, d] # XXXXXX!
                horse_location_and_directions[horse][0], horse_location_and_directions[horse][1] = next_r, next_c

            printMap(current_stacked_horse_map)
            print(horse_location_and_directions)

            # 상태 기록 업데이트
            # horse_location_and_directions[i] # = [r, c, d]

            if len(current_stacked_horse_map[next_r][next_c]) >= 4:
                return turn_count
        turn_count += 1 # 다음 turn 세팅

    return -1

def reversed_direction(d):
    if d % 2 == 0:
        return d+1
    else:
        return d-1

# def move(horse_num, )
def printMap(horse_map):
    for arr in horse_map:
        print(arr)
    print()

# print("정답 = 2 / 현재 풀이 값 = ", get_game_over_turn_count(k, chess_map, start_horse_location_and_directions))

start_horse_location_and_directions = [
    [0, 1, 0],
    [1, 1, 0],
    [0, 2, 0],
    [2, 2, 2]
]
# print("정답 = 9 / 현재 풀이 값 = ", get_game_over_turn_count(k, chess_map, start_horse_location_and_directions))

start_horse_location_and_directions = [
    [0, 1, 0],
    [0, 1, 1],
    [0, 1, 0],
    [2, 1, 2]
]
# print("정답 = 3 / 현재 풀이 값 = ", get_game_over_turn_count(k, chess_map, start_horse_location_and_directions))

import sys
# ---------------------- 입력 처리 ----------------------
raw_input = sys.stdin.read().split()
idx = 0
n = int(raw_input[idx])
idx += 1
k = int(raw_input[idx])
idx += 1

game_map = []
for _ in range(n):
    row = list(map(int, raw_input[idx:idx+n]))
    idx += n
    game_map.append(row)

start_horse_location_and_directions = []
for _ in range(k):
    r = int(raw_input[idx]) - 1
    c = int(raw_input[idx+1]) - 1
    d = int(raw_input[idx+2]) - 1
    idx += 3
    start_horse_location_and_directions.append([r, c, d])

# ---------------------- 결과 출력 ----------------------
print(get_game_over_turn_count(k, game_map, start_horse_location_and_directions))