from collections import deque

# 큐 사용
# 이점: 하나씩 pop 하고 남은 것들만 신경 쓰면(=비교하면) 됨. index 신경 쓸 필요 없음
def get_price_not_fall_periods(prices):
    # prices를 원소로 갖는 queue 생성, 하나씩 pop(left)하며 '남은 것'들과 비교
    # count는 각자의 차례에 loop 안에서 세고 빈 배열에 하나씩 append
    not_fall_counts = []

    queue_prices = deque(prices)

    while queue_prices:
        current_price = queue_prices.popleft()
        not_fall_count = 0
        for price in queue_prices:
            not_fall_count += 1 # 일단 기간 증가
            if current_price > price: # 만약 떨어졌으면, 그만 증가
                break
        not_fall_counts.append(not_fall_count)

    return not_fall_counts

print("정답 = [4, 3, 1, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods([1, 2, 3, 2, 3]))
print("정답 = [6, 2, 1, 3, 2, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods([3, 9, 9, 3, 5, 7, 2]))
print("정답 = [6, 1, 4, 3, 1, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods([1, 5, 3, 6, 7, 6, 5]))