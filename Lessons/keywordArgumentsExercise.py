def getPhone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phoneNumber = getPhone(country=1, area=123, first=456, last=7890)

print(phoneNumber)