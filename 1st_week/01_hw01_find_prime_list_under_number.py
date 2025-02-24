import math
from math import floor

input = 20

# Sieve of Eratosthenes 에라토스테네스의 체

# 1. 에라토스테네스의 채 - 끝까지 탐색(-)하는 버전 + TF 배열(+) 버전
# Time complexity: O(n^2) - 아주 비효율적.
def find_prime_list_under_number_1(number):
    is_primes = [True] * (number+1) # is_primes[number] 존재하도록.
    primes = []

    # 2부터 number까지 돌며
    # true이면 자기 자신은 그대로 두고, 배수들을 false로 변경
    # Number까지 탐색하며 primes의 element 추가 증가
    # return primes
    for num in range(2, number+1):
        if is_primes[num]:
            # element 추가
            primes.append(num)
            # 배수들을 false로 변경
            composite_number = num + num
            while composite_number <= number:
                is_primes[composite_number] = False
                composite_number += num

    return primes


# 2. 에라토스테네스의 채 - Root n까지 탐색(soso)하는 버전 + list(-)
# -> Time: O(n*rootN)
def find_prime_list_under_number_2(number):
    # 2부터 root number까지 돌며
    # 자기 자신은 그대로 두고, 배수들을 제거
    # 0, 1 제거
    # return `primes`
    primes = list(range(number+1))
    # print(primes)
    root_number = math.sqrt(number)
    int_floor_root_number = floor(root_number) # 작거나 같은 정수 - 딱 떨어지는 경우에도 해야 함. 4->2면 2까지 검사해야함 -> range( , intRootNumber+1)

    for num in range(2, int_floor_root_number+1):
        # 배수 제거
        multiple = num + num
        while multiple <= number:
            if multiple in primes:
                primes.remove(multiple)
            multiple += num

    # 0, 1 제거
    primes.remove(0)
    primes.remove(1)

    return primes

# 최종 버전. 에라토스테네스의 채 종결 ver
# 3. 에라토스테네스의 채 - Root n까지 탐색(+)하는 버전 + remove 연산 대신 TF 값 변경(+)
# -> Time: O(N log(log(N)) (최적화된 에라토스테네스의 체)
# 개선1. 비용 큰(O(N)) remove 연산 없애고자 bool 배열인 is_prime 사용
# 개선2. floor() 대신 int() 사용
# 개선3. 배수 제거 시 간략한 for문 사용, num * 2 아닌 num * num부터 시작
def find_prime_list_under_number_optimzed(n):
    # 2부터 root number까지 돌며
    # 자기 자신은 그대로 두고, 배수들을 제거

    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False # 0, 1 제거

    root_n = math.sqrt(n)
    # 작거나 같은 정수 - 딱 떨어지는 경우에도 해야 함. 4->2면 2까지 검사해야함 -> range( , int_root_n+1)
    int_root_n = int(root_n) # floor() 필요 없이 int()로 하면 됨
    for num in range(2, int_root_n + 1):
    # for num in range(2, int(math.sqrt(n))+1):
        if is_prime[num]:
            # 배수 제거 - (1) 길고 장황한 while & if문
            # multiple = num + num
            # while multiple <= number:
            #     if multiple in is_prime:
            #         is_prime.remove(multiple)
            #     multiple += num

            # 배수 제거 - (2) for 문으로 깔끔하게 가능
            # 유의: num * 2부터 시작할 필요 X. 왜냐면 그건 이미 2가 했으므로. 자기 자신의 제곱부터 시작해서 자기 자신을 더해가면 됨.
            for multiple in range(num * num, n + 1, num):
                is_prime[multiple] = False

    primes = []

    for num, prime in enumerate(is_prime):
        if prime: primes.append(num)
    return primes

result = find_prime_list_under_number_optimzed(input)
print(result)