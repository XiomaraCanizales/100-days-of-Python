# Discount a price according to its value
price = 250

if price >= 300:
    print(price - ((price * 30) / 100))
elif price >= 200:
    print(price - ((price * 20) / 100))
elif price >= 100:
    print(price - ((price * 10) / 100))
elif price < 100 and price >= 0:
    print(price - ((price * 5) / 100))
else:
    print('no discount')