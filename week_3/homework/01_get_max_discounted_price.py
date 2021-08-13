shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]

# 가장 많은 할인을 받으려면, 가장 높은 금액을 가장 높은 할인률로 적용하면 된다!
# 내림차순 정렬을 활용해 높은 수가 맨 앞으로 오도록한다

def get_max_discounted_price(prices, coupons):
    coupons.sort(reverse=True)
    prices.sort(reverse=True)
    price_index = 0
    coupon_index = 0
    max_discounted_price = 0

    while price_index < len(prices) and coupon_index < len(coupons):
        max_discounted_price += prices[price_index] * (100 - coupons[coupon_index]) / 100
        price_index += 1
        coupon_index += 1

    while price_index < len(prices):
        max_discounted_price += prices[price_index]
        price_index += 1

    return max_discounted_price


print(get_max_discounted_price(shop_prices, user_coupons))  # 926000 이 나와야 합니다.
print("정답 = 485000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], [10, 70, 30, 20]))
print("정답 = 1550000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], []))
print("정답 = 1458000 / 현재 풀이 값 = ", get_max_discounted_price([20000, 100000, 1500000], [10, 10, 10]))