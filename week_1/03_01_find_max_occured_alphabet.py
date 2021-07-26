input = "hello my name is sparta"


# 각 단어마다 몇개인지 출력해서 비교
def find_max_occurred_alphabet(string):
    alphabet_array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
                      'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                      's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    max_occurrence = 0  #빈도수
    max_alphabet = alphabet_array[0]
    for alphabet in alphabet_array: # N(26)
        occurrence = 0 # 1

        for char in string: # N => N*2
            if char == alphabet: # 1
                occurrence += 1 # 1

        if occurrence > max_occurrence: # 1 => 3
            max_occurrence = occurrence # 1
            max_alphabet = alphabet # 1

    return max_alphabet

    # 시간복잡도 : 26*(1 + (N*2) + 3) = 52N+104 => O(N)


result = find_max_occurred_alphabet(input)
print(result)
