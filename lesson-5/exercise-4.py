my_list = [200, 3, 14, 44, 1, 1, 3, 11, 6, 2, 79, 113, 59]
new_list = [j for i, j in zip(my_list, my_list[1:]) if j > i]
print(new_list)
