my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
my_list_asc = []
for item in my_list:
    my_list_asc.append(item)
    my_list_asc.sort()
print(my_list_asc)
my_list_desc = []
for item in my_list_asc:
    my_list_desc.insert(-item, item)
print(my_list_desc)
my_list_par = my_list_asc[1::2]
print(my_list_par)
my_list_impar = my_list_asc[::2]
print(my_list_impar)
my_list_mult = []
for item in my_list:
    if item%3 == 0:
        my_list_mult.append(item)
print(my_list_mult)