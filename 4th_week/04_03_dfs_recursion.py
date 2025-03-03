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
visited = []


# iteration으로 하면 중첩의 중첩의 중첩..이 될 것 같으므로 재귀를 시도해보기로 함.
def dfs_recursion(adjacent_graph, cur_node, visited_array):
    # 그래프에서 cur_node의 adjacent_node 중 vistied_array에 없는 첫 번째 노드를 찾음
    # visit!
    #   visited_array에 넣고 걔를 cur_node로 두고, adjacent_node 중 vistied_array에 없는 첫 번째 노드를 찾음 <- 재귀
    #   없다면 return
    visited_array.append(cur_node)

    for adjacent_node in adjacent_graph[cur_node]:
        if adjacent_node not in visited_array: # 탐색할 것
            dfs_recursion(adjacent_graph, adjacent_node, visited_array)


dfs_recursion(graph, 1, visited)  # 1 이 시작노드입니다!
print(visited)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 이 출력되어야 합니다!