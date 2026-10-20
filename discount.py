def calculate_discount(price, percent):
    discount_amount = price * (percent / 100)
    return price - discount_amount

print(calculate_discount(100, 10))   # 90.0
print(calculate_discount(250, 20))   # 200.0
print(calculate_discount(59.99, 15)) # 50.9915