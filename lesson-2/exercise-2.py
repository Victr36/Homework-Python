list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
new_list = []

for el in list:
    if el.isdigit():
        num = int(el)
        new_list.extend(['"', f'{num:02d}', '"'])
    elif (el.startswith('-') or el.startswith('+')) and el[1:].isdigit():
        num = int(el[1:])
        new_list.extend(['"', f'{el[0]}{num:02d}', '"'])
    else:
        new_list.append(el)
    new_list.append(' ')
print(new_list)
list_2 = ' '.join(new_list).strip()
print(list_2)

