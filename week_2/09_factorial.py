def factorial(n):
    # 이 부분을 채워보세요!
    if n == 1:  #빠져나올 타이밍!
        return 1
    return n * factorial(n-1)


print(factorial(5))