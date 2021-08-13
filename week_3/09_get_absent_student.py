all_students = ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"]
present_students = ["정연", "모모", "채영", "쯔위", "사나", "나연", "미나", "다현"]

#반복 -> 비효율적
#딕셔너리 사용! -> 공간복잡도가 많아짐

def get_absent_student(all_array, present_array):
    student_dict = {}

    for key in all_array:  #all_array 키를 하나씩 등록
        student_dict[key] = True #공간복잡도 O(N)

    for key in present_array: #비교대상 배열을 삭제시킨다
        del student_dict[key]

    for key in student_dict.keys(): #남은 키를 반환
        return key


print(get_absent_student(all_students, present_students))