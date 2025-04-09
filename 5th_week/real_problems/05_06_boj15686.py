from itertools import combinations

def get_min_city_chicken_distance(n, m, city_map):
    houses = []

    # 치킨집 조합 구하기 e.g. [  [(1,2), (3,4), ...( , )], [ ], ...  ]

    # houses 구함 + 현재 chickens 추출
    current_chickens = []
    for i in range(n):
        for j in range(n):
            if city_map[i][j] == 1:
                houses.append((i, j))
            elif city_map[i][j] == 2:
                current_chickens.append((i, j))

    chickens_combinations = list(combinations(current_chickens, m))

    min_city_chicken_distance = 2*n * 2*n # FIXME: 초기 최댓값 잘못 지정했었음. 최대 거리 * 최대 집 개수 = 2N * 2N

    for chickens in chickens_combinations:
        min_city_chicken_distance = min(min_city_chicken_distance, get_chicken_distance_of_city(chickens, houses, n))
    return min_city_chicken_distance

# 도시의 치킨거리 (chickens: list임) [(x1, y1), ...( , ) ]
def get_chicken_distance_of_city(chickens, houses, n):
    # houses = [] # [(x, y), ...]
    chicken_distance = 0
    for x, y in houses:
        chicken_distance += get_chicken_distance_of_house(x, y, chickens, n)

    return chicken_distance

# chickens가 치킨집들의 좌표일 때,
# 집 하나의 치킨거리 (chickens: list임) [(x1, y1), ...( , ) ]
def get_chicken_distance_of_house(x, y, chickens, n):
    min_distance = 2*n
    # print("min_distance", min_distance)
    for xc, yc in chickens:
        min_distance = min(min_distance, get_distance(x, y, xc, yc))

    return min_distance

def get_distance(x1,y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)

# 입력 처리
import sys
input = sys.stdin.read


data = input().split()
n, m = int(data[0]), int(data[1])
city_map = []
index = 2
for _ in range(n):
    row = list(map(int, data[index:index + n]))
    city_map.append(row)
    index += n

result = get_min_city_chicken_distance(n, m, city_map)
print(result)