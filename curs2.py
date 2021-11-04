my_var = 5
msg = "Nimic"
if my_var > 6:
    msg = "Set instructiuni 1"
elif my_var > 10:
    msg = "Set instructiuni 2"
print(msg)

# var = sintaxa_then if conditie else sintaxa_else
a = 1
b = 2
x = 1 if a > b else -1
print(x)

while True:
    print("Set instructiuni")
    break

for i in range(10):
    print(f"Set {i}")  # 0 -> 9

# variabila = "Ana are mere"
# for i in variabila:
    # print(i)
    # lista.append(i)

# lista = [i for i in variabila]
# print(lista)

# for item, value in enumerate(variabila):
# print(f"{item} => {value}")

# dictionar = {"key1": "value1", "key2": "value2"}
# for item in dictionar.items():
#   print(item)
#    item0, item1 = item
#    print(item0, item1)

# variabila = ('1', '2')
# print(type(variabila))

variabila = "Ana are \"mere\""
print(variabila)