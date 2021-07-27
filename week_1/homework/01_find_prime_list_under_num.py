input = 20


def find_prime_list_under_number(number):
    prime_list = [] #담을 배열을 생성하는 것이 중요!

    for n in range(2, number + 1):
        for i in prime_list:
            if n % i == 0 and i * i <= n: # 제곱근이 작을때 까지 추가!
                break
        else:
            prime_list.append(n)

    return prime_list


result = find_prime_list_under_number(input)
print(result)
