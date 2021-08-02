finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

#이진탐색 O(logN)
def is_existing_target_number_binary(target, array):
    # 구현해보세요!
    current_min = 0  #최소
    current_max = len(array)-1  #최대
    current_guess = (current_min+current_max)//2  #가운데 값

    while current_min <= current_max:
        if array[current_guess] == target: #타겟, 가운데 값이 같으면 바로 반환
            return True
        elif array[current_guess] < target: #타겟이 가운데 값보다 크면 위에 탐색
            current_min = current_guess+1
        else:
            current_max = current_guess-1 #타겟이 가운데 값보다 크면 아래 탐색

        current_guess = (current_min+current_max)//2  #새로 최대, 최소값 업데이트!!
    return False


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)