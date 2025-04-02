from collections import deque

def doll_claw_machine(board, moves):
    bucket = []
    num_removed = 0

    # board -> queue N개로 변환
    queues = []
    for j in range(len(board[0])):
        queue = deque()
        for i in range(len(board)):
            if board[i][j] == 0: continue
            queue.append(board[i][j])
        queues.append(queue)


    # moves 돌면서 해당 큐 popLeft, 바구니 stack peek()(=last)과 같으면 바구니 pop, 다르면 바구니에 append
    for move in moves:
        queue_num = move - 1
        if not queues[queue_num]: # 비었으면 다음 move로 넘어감
            continue

        picked_doll = queues[queue_num].popleft()
        if bucket and bucket[-1] == picked_doll:
            bucket.pop()
            num_removed += 2
            continue

        # 다르거나 bucket 비었으면
        bucket.append(picked_doll)

    return num_removed


board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

print("정답: 4, 결과:", doll_claw_machine(board, moves))