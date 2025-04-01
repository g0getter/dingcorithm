import sys


def print_board(board):
    print("BOARD")
    for row in board:
        print(row)


def read_input(input_data):
    if input_data is None:
        # 백준에서 실행할 때
        read_line = sys.stdin.readline
    else:
        # 테스트할 때 (문자열 입력)
        input_lines = input_data.strip().split("\n")
        read_line = lambda: input_lines.pop(0)

    # 첫 번째 줄 입력 (보드 크기 N, 말의 개수 K)
    N, K = map(int, read_line().split())

    # 보드 정보 입력 (N x N)
    board = [list(map(int, read_line().split())) for _ in range(N)]

    # 말 정보 입력 (K개)
    horses = []
    for _ in range(K):
        x, y, d = map(int, read_line().split())
        horses.append([x - 1, y - 1, d])  # 인덱스를 0부터 시작하도록 조정

    return N, K, board, horses


def new_game2(input):
    # "이동". status_board 업데이트, status_horses 업데이트, 말 개수 반환
    def move(horse_num, next_board):
        nx, ny = next_board
        # 옯길 것: 나와 위의 것
        hx, hy, hd = status_horses[horse_num]
        h_index = status_board[hx][hy].index([horse_num, hd])
        horses_to_top = status_board[hx][hy][h_index:]

        status_board[nx][ny] += horses_to_top # 옮김
        status_board[hx][hy] = status_board[hx][hy][:h_index] # 떼어냄

        # horse 상태 업데이트
        for h_num, h_d in horses_to_top:
            status_horses[h_num] = [nx, ny, h_d]


        return len(status_board[nx][ny])


    N, K, board, horses = read_input(input)

    # 입력 확인용 (테스트)
    print("N:", N)
    print("K:", K)
    print("Board:")
    for row in board:
        print(row)
    print("Horses:")
    for horse in horses:
        print(horse)

    # 필요한 것 생성
    status_horses = horses # [[x, y, direction], ...]
    status_board = [[ [] for _ in range(N)] for _ in range(N)] # 내부: [(말 번호, 방향), ...] -> [[말 번호, 방향], ...]
    round = 0

    # status_board 세팅
    for horse_num, (x, y, d) in enumerate(status_horses):
        status_board[x][y].append([horse_num, d])

    print_board(status_board)

    while round <= 1000:
        round += 1
        print("ROUND", round)
        # 1. 다음 칸 구함, 이동
        for horse_num, (x, y, direction) in enumerate(horses):
            print("HORSE", horse_num)
            next_x, next_y = next_board(x, y, direction, N)
            horses_num = 0
            if next_x == -1 or board[next_x][next_y] == 2: # 파 Or 벗어남
                print("벗어남!")
                # 이동 방향 Reverse
                new_direction = change_direction(status_horses[horse_num][2]) # new direction
                # status_horses 업데이트
                status_horses[horse_num][2] = new_direction
                # status_board 업데이트
                h_index = status_board[x][y].index([horse_num, direction])
                status_board[x][y][h_index] = [horse_num, new_direction]


                nnx, nny = next_board(x, y, status_horses[horse_num][2], N)
                if nnx == -1 or board[nnx][nny] == 2: # 파 Or 벗어남
                    print_board(status_board)
                    continue # 아무 일도 안 일어남
                else:
                    horses_num = move(horse_num, (nnx, nny))
            elif board[next_x][next_y] == 0: # 흰
                horses_num = move(horse_num, next_board = (next_x, next_y))
            elif board[next_x][next_y] == 1:  # 빨: Reverse & 이동
                status_board[next_x][next_y] = list(reversed(status_board[next_x][next_y]))
                horses_num = move(horse_num, next_board=(next_x, next_y))

            print_board(status_board)

            if horses_num >= 4:
                return round

    return -1

def change_direction(direction):
    if direction == 1: return 2
    elif direction == 2: return 1
    elif direction == 3: return 4
    elif direction == 4: return 3




def next_board(x, y, direction, N):
    new_x, new_y = x, y
    if direction == 1:
        new_y += 1
    elif direction == 2:
        new_y -= 1
    elif direction == 3:
        new_x -= 1
    elif direction == 4:
        new_x += 1

    if 0 <= new_x < N and 0 <= new_y < N:
        return new_x, new_y
    else:
        return -1, -1 # 영역 벗어남


input1 = """
4 4
0 0 2 0
0 0 1 0
0 0 1 2
0 2 0 0
2 1 1
3 2 3
2 2 1
4 1 2
"""
input2 = """
4 4
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
1 1 1
1 2 1
1 3 1
1 4 1
"""
input3 = """
4 4
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
1 1 1
1 2 1
1 3 1
2 4 3
"""
input4 = """
4 4
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
1 1 1
1 2 1
1 3 1
3 3 3
"""
input5 = """
6 10
0 1 2 0 1 1
1 2 0 1 1 0
2 1 0 1 1 0
1 0 1 1 0 2
2 0 1 2 0 1
0 2 1 0 2 1
1 1 1
2 2 2
3 3 4
4 4 1
5 5 3
6 6 2
1 6 3
6 1 2
2 4 3
4 2 1
"""
print(new_game2(input5))

