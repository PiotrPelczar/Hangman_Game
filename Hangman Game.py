mysteryword = "wizzard"
no_of_tries = 12
import sys

used_letters = []
user_word = []
for _ in mysteryword:
    user_word.append("_")

def find_indexes (mysterword, letter):
    indexes = []
    for index, letter_in_word in enumerate(mysteryword):
        if letter == letter_in_word:
            indexes.append(index)

    return indexes

    ##

while True:
    letter = input("Try some letter: ")
    used_letters.append(letter)

    found_indexes = find_indexes(mysteryword, letter)

    if len(found_indexes) == 0:
        print("No such letter in the word")
        print(user_word)
        no_of_tries -= 1
        print("Number of tries left: " + str(no_of_tries))
        if no_of_tries == 0:
            print("Game over")
            sys.exit(0)


    else:
        for index in found_indexes:
            user_word[index] = letter
            print(user_word)
            no_of_tries -= 1
            print("Number of tries left: " + str(no_of_tries))

            if "".join(user_word) == mysteryword:
                print("Congratulations, you won!")
                sys.exit(0)

            if no_of_tries == 0:
                print("Game over")
                sys.exit(0)



    print("Letters used so far: ", used_letters)







