from collections import deque

def solution(board, moves):
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
        if not queues[queue_num]: # 비었으면 다음 move로 넘어감(예외 먼저 처리)
            continue

        picked_doll = queues[queue_num].popleft()
        if bucket and bucket[-1] == picked_doll: # bucket의 가장 마지막 인형과 비교
            bucket.pop()
            num_removed += 2
        else: # 다르거나 bucket 비었으면
            bucket.append(picked_doll)

    return num_removed