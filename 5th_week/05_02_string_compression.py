

# 1. 1개 단위로 자름 -> 몇 개로 줄어드는지 확인, 2개 단위로 자름 -> 확인, ... , N/2개 단위 -> 확인
# 2. 1의 최솟값 반환
# <N개 단위로 자르기> 함수
# 1. 앞 N개를 변수 pattern으로 저장
# 2. 다음 N개를 pattern과 비교
# 2-1. 같 -> count +1
# 2-2. 다 -> 압축했다는 새로운 변수에 <count><pattern>으로 넣고 pattern 이번 것으로 변경
def string_compression(string):
    min_length = len(string)
    for n in range(1, len(string)//2+1):
        new_length = compressed_length(string, n)
        if min_length > new_length:
            min_length = new_length
    return min_length

def compressed_length(string, n):
    new_string = ""
    pattern = ""
    count = 0

    i = 0
    while i < len(string): # TODO: i+n으로 기준?
        # print("from", i, "to", i+n, "among", len(string))
        if pattern == string[i:i+n]: # 같음
            count += 1
        else: # 다름
            if count > 1:
                new_string += str(count)
            new_string += pattern
            pattern = string[i:i+n] # 패턴 초기화
            count = 1 # count 초기화
        # print("new_string",new_string)
        i += n

    # 마지막 것 처리 (TODO: 더 간결하게)
    if count > 1:
        new_string += str(count)
    new_string += pattern

    # print("compressed string", new_string, "n:", n)
    return len(new_string)



print("정답 = 14 / 현재 풀이 값 = ", string_compression("abcabcabcabcdededededede"))
print("정답 = 3 / 현재 풀이 값 = ", string_compression("JAAA"))
print("정답 = 9 / 현재 풀이 값 = ", string_compression("AZAAAZDWAAA"))
print("정답 = 12 / 현재 풀이 값 = ", string_compression('BBAABAAADABBBD'))