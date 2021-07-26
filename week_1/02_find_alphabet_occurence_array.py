# 알파벳 빈도수 최대값
def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26
    for char in string:
        if not char.isalpha():  #문자가 아니면 패스!
            continue
        arr_index = ord(char) - ord('a')  # a->0, b->1, c_>2 로 바꾸기
        alphabet_occurrence_array[arr_index] += 1

    return alphabet_occurrence_array


print(find_alphabet_occurrence_array("hello my name is sparta"))