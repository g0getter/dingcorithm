input = "abcba"

# 양 끝 2개 비교 && 안의 함수 결과
def is_palindrome(string):
    if len(string) <= 1: return True

    return (string[0] == string[-1]) and is_palindrome(string[1:-1])
    # string[1:-1] == string[1:len(string)-1]


print(is_palindrome(input))