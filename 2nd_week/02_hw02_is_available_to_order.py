shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


def is_available_to_order(menus, orders):
    # 1. menus를 모두 돌면서 orders와 일치하는 것이 있는지 확인. 있으면 orders에서 제거 -> 최악 시 O(m*n)
    # 2. 일단 둘 다 정렬하고 / 각 포인터로 둘을 비교하는데 일치하면 둘 중 순서가 빠른 것의 포인터를 하나 보냄
    # 3. (수업 최종 답안) 자료구조를 Set으로 변경 -> Set로 변경에 O(M), orders 탐색애 O(N) -> O(M+N)
    set_menus = set(menus)

    for order in orders:
        if order not in set_menus: return False

    return True


result = is_available_to_order(shop_menus, shop_orders)
print(result)

# 참고: python의 in 연산자 - list에서는 O(N) 소요(https://wiki.python.org/moin/TimeComplexity), set은 O(1)