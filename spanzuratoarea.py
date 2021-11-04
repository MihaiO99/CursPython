# word = "onomatopee"
import random
from random_word import list_of_random_words
word = random.choice(list_of_random_words)
word_list = []
for item in word:
    if item != word[0] and item != word[-1]:
        word_list.append('_')
    else:
        word_list.append(item)
print(" ".join(word_list))
count_nr = 1
list_already_checked = []
new_word = " ".join(word_list)
while count_nr <= 7:
    user_letter = input("Alege o litera: ").lower()
    if user_letter == "":
        print("Introdu o litera!")
        continue
    if user_letter in word_list:
        print("Litera este deja!")
    elif user_letter in list_already_checked:
        print(f"Litera a fost incercata! Literele incercate sunt: {', '.join(list_already_checked)}")
    else:
        if user_letter in word:
            for iterator, value in enumerate(word):
                if user_letter == value:
                    word_list[iterator] = user_letter
            print(" ".join(word_list))
        else:
            count_nr += 1
            if count_nr < 8:
                print(f"Mai ai {8 - count_nr} incercari!")
        list_already_checked.append(user_letter)
        if "".join(word_list) == word:
            print("Felicitari! Ai castigat!")
            break
        elif count_nr > 7:
            print(f"Ai pierdut! Cuvantul era {word}")