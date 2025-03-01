shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]


# 가장 비싼 price에 가장 높은 coupon 적용
# -> 높은 순서로 정렬, 가장 높은 것에 가장 높은 coupon 적용해서 계산 결과 도출
def get_max_discounted_price(prices, coupons):
    prices.sort(reverse=True)
    coupons.sort()

    total = 0

    for price in prices:
        discount_percentage = 0
        if len(coupons) > 0:
            discount_percentage = coupons.pop()
        total += price * (100-discount_percentage)/100
    return int(total)


print("정답 = 926000 / 현재 풀이 값 = ", get_max_discounted_price([30000, 2000, 1500000], [20, 40]))
print("정답 = 485000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], [10, 70, 30, 20]))
print("정답 = 1550000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], []))
print("정답 = 1458000 / 현재 풀이 값 = ", get_max_discounted_price([20000, 100000, 1500000], [10, 10, 10]))