# 위의 그래프를 예시로 삼아서 인접 리스트 방식으로 표현했습니다!
graph = {
    1: [2, 5, 9],
    2: [1, 3],
    3: [2, 4],
    4: [3],
    5: [1, 6, 8],
    6: [5, 7],
    7: [6],
    8: [5],
    9: [1, 10],
    10: [9]
}


def dfs_stack(adjacent_graph, start_node):
    # adjacent node 중 visited가 아닌 노드를 stack에 저장
    # stack에서 하나 pop, 그의 adjacent node 중 visited가 아닌 노드를 stack에 저장 - 반복됨.
    # adjacent node가 없으면 자연스럽게 return
    visited = []
    stack_node_to_visit = []

    stack_node_to_visit.append(start_node)

    while len(stack_node_to_visit) > 0:
    # while stack_node_to_visit: # 동일
        # 하나 꺼내고
        node_to_visit_next = stack_node_to_visit.pop()
        # 방문하고
        visited.append(node_to_visit_next)
        # (인접노드) 다 넣고
        for adjacent_node in adjacent_graph[node_to_visit_next]:
            if adjacent_node not in visited:
                stack_node_to_visit.append(adjacent_node)

        # ---> stack_node_to_visit이 빌 때까지 반복

    return visited


print(dfs_stack(graph, 1))  # 1 이 시작노드입니다!
# [1, 9, 10, 5, 8, 6, 7, 2, 3, 4] 이 출력되어야 합니다!