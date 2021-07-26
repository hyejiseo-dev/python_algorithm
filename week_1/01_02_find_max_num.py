input = [3, 5, 6, 1, 2, 4]

def find_max_num(array):
    # 이 부분을 채워보세요!
    max_num = array[0]  #초기값 설정, 하나씩 비교해보기
    for num in array:
        if num > max_num:
            max_num = num

    return max_num


print("정답 = 6 / 현재 풀이 값 = ", find_max_num([3, 5, 6, 1, 2, 4]))
print("정답 = 6 / 현재 풀이 값 = ", find_max_num([6, 6, 6]))
print("정답 = 1888 / 현재 풀이 값 = ", find_max_num([6, 9, 2, 7, 1888]))
