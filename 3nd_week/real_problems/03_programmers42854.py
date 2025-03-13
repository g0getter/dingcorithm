# 문제 설명 보충 #
# 떨어지지 않았다: 본인 기준으로 더 작지 않다(크거나 같다). 근데 한 번 떨어지면 끝. 그때부터는 이미 떨어진 기간으로 치부해서 더 이상 기간을 증가시키지 X
# 바로 값이 내려가도 1초간 떨어지지 않은 것임.
def solution(prices):
    # 같은 크기의 배열 생성, 돌면서 각자 본인보다 크거나 같으면 +1. -> O(n^2)
    not_fall_counts = [0] * len(prices)

    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            not_fall_counts[i] += 1 # 일단 기간 증가
            if prices[i] > prices[j]: # 만약 떨어졌으면, 그만 증가
                break

    return not_fall_counts

print("answer: ", [4, 3, 1, 1, 0])
print(solution([1, 2, 3, 2, 3]))