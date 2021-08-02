input = "abcba"

# 일반 함수 풀이
# def is_palindrome(string):
#     n = len(string)
#     for s in range(n):
#         if string[s] != string[n-1-s]:
#             return False
#     return True

#재귀함수

def is_palindrome(string):
    if len(string) <= 1: #한글자면 회문!
        return True
    if string[0] != string[-1]:
        return False
    return is_palindrome(string[1:-1])


print(is_palindrome(input))