from collections import deque


# KEY POINT 1. 완전 탐색 -> bfs -> queue, "VISITED" 배열 필요
# HARD POINT. queue와 visited 배열을 어떤 형태로 구성할지.
# KEY POINT 2. (bfs 쓰는)brown을 먼저 채우고 cony를 (time 기반으로.->따로 저장할 필요 없음) 계산해서 한 time에 대해 한꺼번에(한 번에) 확인.

def catch_me(cony_pos, brown_pos):
    # cf.cony 기준, 시간 -> 따로 저장하지 않음. 같은 시간일 때 b를 구할 수 있다면 그때그때 확인하면 되므로.
    # visited 배열 -> bfs를 쓰는 brown의 visited 배열. visited[position][time] = (Bool)
    # (cf.{time: position}인 cony_dict가 아니라!)
    brown_visited = [{} for _ in range(200001)] # dictionary의 배열
    brown_queue = deque() # (position, time)

    # cf.cony_dict 만들기 -> 필요 없음. 그때그때 확인

    # cf.brown 만들기 - 같은 t에 대해 한꺼번에 확인(cony 위치와 일치하는 게 있는지)
    brown_queue.append((brown_pos, 0))

    ## pop, enqueue하며 brown_visited 채움, brown(t+1일 때)과 cony(t+1)일 때를 비교
    while brown_queue:
        position, time = brown_queue.popleft()

        ## time+1일 때의 brown 위치 3가지 넣기
        new_time = time + 1

        # 1. position - 1
        new_position = position - 1
        if new_position >= 0 and new_time not in brown_visited[new_position]: # 추가함
            brown_queue.append((new_position, new_time))
            brown_visited[new_position][new_time] = True

        # 2. position + 1
        new_position = position + 1
        if new_position < 200001 and new_time not in brown_visited[new_position]:
            brown_queue.append((new_position, new_time))
            brown_visited[new_position][new_time] = True

        # 3. position * 2
        new_position = position * 2
        if new_position < 200001 and new_time not in brown_visited[new_position]:
            brown_queue.append((new_position, new_time))
            brown_visited[new_position][new_time] = True


        ## cony가 new_time(=t+1)일 때 위치와 일치하는지 확인

        # 그 전에, 필요 시 cony_pos 업데이트
        # 이번 loop가 brown 입장에서 `time`의 마지막 loop가 아니라면(=다음 것도 같은 time일 때라면) continue, 이번 time의 마지막이면 업데이트
        if brown_queue and brown_queue[0][1] == time:
            continue
        else:
            cony_pos += new_time

        # print(f"cony_pos: {cony_pos}, new_time: {new_time}")

        # print(brown_queue)
        if new_time in brown_visited[cony_pos] and brown_visited[cony_pos][new_time]:
            # print(f"brown_visited[{cony_pos}][{new_time}]: {brown_visited[cony_pos][new_time]}")
            return new_time

    return

print("정답 = 5 / 현재 풀이 값 = ", catch_me(11,2))
print("정답 = 3 / 현재 풀이 값 = ", catch_me(10,3))
print("정답 = 8 / 현재 풀이 값 = ", catch_me(51,50))
print("정답 = 28 / 현재 풀이 값 = ", catch_me(550,500))