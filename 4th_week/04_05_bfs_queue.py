# 위의 그래프를 예시로 삼아서 인접 리스트 방식으로 표현했습니다!
graph = {
    1: [2, 3, 4],
    2: [1, 5],
    3: [1, 6, 7],
    4: [1, 8],
    5: [2, 9],
    6: [3, 10],
    7: [3],
    8: [4],
    9: [5],
    10: [6]
}

# 뒤에 나오는 인접한 것들이 이전 것들을 덮으면 안됨. -> 이전 것들 먼저 방문 필요 -> 큐로 해보기
def bfs_queue(adj_graph, start_node):
    # 자신을 pop() 후 인접한 것들 넣고 ---> 다 빌 때까지 반복
    queue_to_visit_next = [start_node]
    visited = []

    while queue_to_visit_next:
        node_to_visit_next = queue_to_visit_next.pop(0)
        visited.append(node_to_visit_next)
        for adjacent_node in adj_graph[node_to_visit_next]:
            if adjacent_node not in visited:
                queue_to_visit_next.append(adjacent_node)
        # 다 넣었으면 본인 빼고, 인접노드들 넣고, ... 반복

    return visited


print(bfs_queue(graph, 1))  # 1 이 시작노드입니다!
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 이 출력되어야 합니다!