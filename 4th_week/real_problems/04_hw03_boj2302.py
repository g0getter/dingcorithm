import sys

# (1)~(4) 각각의 연속된 자리를 배치하는 방법을 구해서 곱하기
# [  _  V  _  V _ _ V ... ]
# [ (1) V (2) V (3) V (4) ]
def get_all_ways_of_theater_seat(total_count, fixed_seat_array):
    if len(fixed_seat_array) == 0 :
        return get_ways_of_consecutive_seat(total_count)
    
    first_consecutive_seat_count = fixed_seat_array[0]-1 # (1)
    answer = get_ways_of_consecutive_seat(first_consecutive_seat_count)
    for i in range(1,len(fixed_seat_array)):
        seat_count = fixed_seat_array[i]-fixed_seat_array[i-1]-1 # (2), (3)
        answer *= get_ways_of_consecutive_seat(seat_count)

    # 마지막 vip 좌석부터 마지막 자리까지
    last_vip_seat = fixed_seat_array[len(fixed_seat_array)-1] # (4)
    answer *= get_ways_of_consecutive_seat(total_count-last_vip_seat)

    return answer

ways = {
    1: 1,
    2: 2
}
def get_ways_of_consecutive_seat(count):
    if count <= 0: return 1
    if count in ways:
        return ways[count]

    # if not,
    ways[count] = get_ways_of_consecutive_seat(count-1) + get_ways_of_consecutive_seat(count-2)
    return ways[count]

# 입력 받기
total_seat_count = int(sys.stdin.readline()) # N
vip_seat_count = int(sys.stdin.readline()) # M
vip_seat_array = [int(sys.stdin.readline()) for _ in range(vip_seat_count)]

# 결과 출력
print(get_all_ways_of_theater_seat(total_seat_count, vip_seat_array))