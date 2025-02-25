input = "aba"


# Two independent pointer(비추)
def is_palindrome_two_independent_pointer(string):
    leftPointer = 0
    rightPointer = len(string)-1

    while leftPointer < rightPointer:
        if string[leftPointer] != string[rightPointer]:
            return False
        leftPointer += 1
        rightPointer -= 1

    return True

def is_palindrome_two_dependent_pointer(string):

    for i in range(len(string)//2):
        if string[i] != string[len(string)-1-i]:
            return False
    return True


print(is_palindrome_two_dependent_pointer(input))