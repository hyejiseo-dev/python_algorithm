input = "abacabade"


def find_not_repeating_character(string):
    alphabet_occurrence_array = [0] * 26
    for char in string:  # N
        if not char.isalpha():  # 문자가 아니면 패스! 1
            continue
        arr_index = ord(char) - ord('a')  # a->0, b->1, c_>2 로 바꾸기 1
        alphabet_occurrence_array[arr_index] += 1  # 1
    not_repeating_character_array = []

    for index in range(len(alphabet_occurrence_array)):
        alphabet_occurrence = alphabet_occurrence_array[index]
        if alphabet_occurrence == 1:
            not_repeating_character_array.append(chr(index + ord('a')))

    for char in string:  #들어온 문자 순서대로 반환하기 위함!
        if char in not_repeating_character_array:
            return char

result = find_not_repeating_character(input)
print(result)