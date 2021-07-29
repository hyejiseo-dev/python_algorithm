# input = [3, 5, 6, 1, 2, 4]

# def find_max(arr):
#     # 첫번째 수를 기준으로 배열의 다음수와 비교하기
#     max_num = arr[0]
#     for num in arr:
#         if num > max_num:
#             max_num = num
#
#     return max_num
#
# print(find_max(input))


# string = "hello my name is sparta"
#
# def find_alphabet_max(str):
#     alpha_arr = [0]*26  # 알파벳 개수 만큼의 초기화 배열 만들기
#     for char in str:
#         if not char.isalpha():  # 문자인지 확인
#             continue
#         arr_index = ord(char) - ord('a')  # 아스키코드로 바꿔서 위치를 반환
#         alpha_arr[arr_index] += 1  # 해당 위치의 인덱스를 증가시킴
#
#
#     return alpha_arr
#
# print(find_alphabet_max(string))

# input = [3, 5, 6, 1, 2, 4]
#
# def find_max_num(array):
#     # 이 부분을 채워보세요!
#     for num in array:
#         for compare_num in array:
#             if num < compare_num:
#                 break
#         else:
#             return num
#
#
# print(find_max_num(input))









