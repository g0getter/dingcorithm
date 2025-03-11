all_students = ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"]
present_students = ["정연", "모모", "채영", "쯔위", "사나", "나연", "미나", "다현"]


# dictionary 사용 -> O(N) (del 연산은 평균적으로 1)
def get_absent_student(all_array, present_array):
    dict_all_students = {}
    for student in all_array:
        dict_all_students[student] = True # 어떤 값이든 상관 없음

    for student in present_array:
        del dict_all_students[student]

    # => dict_all_students에 element 1개만 남음
    for key in dict_all_students.keys():
        return key
    # dict.keys()는 dict_keys를 반환. -> dict_all_students.keys()[0] 같은 리스트 인덱싱을 직접 사용할 수 없음
    # 한 줄로? return next(iter(dict_all_students.keys()))

# in/not in 사용(dictionary든 array든) -> O(N^2)
def shorter_get_absent_student(all_array, present_array):
    for student in all_array:
        if student not in present_array:
            return student


print(get_absent_student(all_students, present_students))
print("정답 = 예지 / 현재 풀이 값 = ", get_absent_student(["류진","예지","채령","리아","유나"],["리아","류진","채령","유나"]))
print("정답 = RM / 현재 풀이 값 = ", get_absent_student(["정국","진","뷔","슈가","지민","RM"],["뷔","정국","지민","진","슈가"]))