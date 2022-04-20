price = [60.1, 80, 33.58, 90, 34, 69.99, 34.65, 55, 89.96, 90.3, 77, 95.76, 65, 88.99, 46, 12.12, 33]

new_list = []
for i in price:
    rubles = int(i)
    diff = round((i - rubles) * 100)
    new_list.append(f'{rubles} руб {diff:02d} коп')
print(", ".join(new_list))
id1 = id(price)
price.sort()
print(price)
print(id(price) == id1)
my_list = sorted(price, reverse=True)
print(sorted(my_list[:5]))
