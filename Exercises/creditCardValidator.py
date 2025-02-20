sumOddDigits = 0
sumEvenDigits = 0
total = 0

cardNumber = input("Enter a credit card #: ")
cardNumber = cardNumber.replace("-", "")
cardNumber = cardNumber.replace(" ", "")
cardNumber = cardNumber[::-1]

for x in cardNumber[::2]:
    sumOddDigits += int(x)

for x in cardNumber[1::2]:
    x = int(x) * 2
    if x >= 10:
        sumEvenDigits += (1+(x % 10))
    else:
        sumEvenDigits += x

total = sumEvenDigits + sumOddDigits

if total % 10 == 0:
    print("VALID")
else:
    print("INVALID")