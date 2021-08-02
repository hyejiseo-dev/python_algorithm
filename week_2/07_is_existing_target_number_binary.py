finding_target = 2
finding_numbers = [0, 3, 5, 6, 1, 2, 4]


# 이진탐색을 사용하지 못한다 > 정렬이 되어 있어야 가능!!
def is_exist_target_number_binary(target, numbers):
    # 이 부분을 채워보세요!
   # numbers = sorted(numbers)

    min_n = 0
    max_n = len(finding_numbers) - 1
    medium_n = (min_n + max_n) // 2

    while min_n <= max_n:
        if numbers[medium_n] == target:
            return True
        elif numbers[medium_n] < target:
            min_n = medium_n + 1
        else:
            max_n = medium_n - 1
        medium_n = (min_n + max_n) // 2
    return False


result = is_exist_target_number_binary(finding_target, finding_numbers)
print(result)
