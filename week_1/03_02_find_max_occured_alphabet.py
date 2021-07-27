
input = "hello my name is sparta"


# 각 단어마다 몇개인지 출력해서 비교
def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0] * 26
    for char in string: # N
        if not char.isalpha():  # 문자가 아니면 패스! 1
            continue
        arr_index = ord(char) - ord('a')  # a->0, b->1, c_>2 로 바꾸기 1
        alphabet_occurrence_array[arr_index] += 1 # 1

    max_occurrence = 0 # 1
    max_alphabet_index = 0 # 1
    for index in range(len(alphabet_occurrence_array)): # 26
        alphabet_occurence = alphabet_occurrence_array[index] # 1
        if alphabet_occurence > max_occurrence: # 1
            max_alphabet_index = index #1
            max_occurrence = alphabet_occurence[index] #1
        print(max_alphabet_index)

   # 시간복잡도 : N(1+2)+1+26(1+3) = 3N + 106 => O(N)

result = find_max_occurred_alphabet(input)
print(result)