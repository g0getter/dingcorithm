input = "0001100"

# My solution: 0과 1 중 적은 덩어리 개수 세기 (수업과 대체로 비슷, 내 구현이 더 이해하기 쉬운듯!)
def find_count_to_turn_out_to_all_zero_or_all_one(string):
    chunk0_num = 0
    chunk1_num = 0
    previous_char = -1

    # 일단 0이든 1이든 만나면 해당 개수 +1
    # '달라지면' 그 chunk +1
    # 마지막에 둘 중 최솟값 반환(둘 중 하나는 0이라면 return 0)

    for current_char in string:
        if previous_char != current_char:
            previous_char = current_char
            if current_char == "0":
                chunk0_num += 1
            else: #"1"
                chunk1_num += 1

    return min(chunk0_num, chunk1_num)


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)