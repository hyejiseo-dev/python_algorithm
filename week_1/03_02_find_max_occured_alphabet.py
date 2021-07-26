input = "hello my name is sparta"


# 각 단어마다 몇개인지 출력해서 비교
def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0] * 26
    for char in string:
        if not char.isalpha():  # 문자가 아니면 패스!
            continue
        arr_index = ord(char) - ord('a')  # a->0, b->1, c_>2 로 바꾸기
        alphabet_occurrence_array[arr_index] += 1

    max_occurrence = 0
    max_alphabet_index = 0
    for index in range(len(alphabet_occurrence_array)):
        alphabet_occurence = alphabet_occurrence_array[index] #0 -> ㅁ
        if alphabet_occurence > max_occurrence:
            max_alphabet_index = index
            max_occurrence = alphabet_occurence[index]
        print(max_alphabet_index)



result = find_max_occurred_alphabet(input)
print(result)
