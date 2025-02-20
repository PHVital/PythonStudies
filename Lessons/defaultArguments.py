def netPrice(listPrice, discount = 0, tax = 0.05):
    return listPrice * (1 - discount) * (1 + tax)

netPrice(500)