from functools import reduce

prices = [19.99, 1.00, 5.75, 12.99, 10.99]

total = reduce(lambda x, y: x + y, prices)

print(f"${total}")