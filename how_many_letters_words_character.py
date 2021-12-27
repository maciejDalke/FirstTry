print("How many letters/words/characters in phrase program")
all_choice = False

# simple one with writing string
user_chose = "o"
user_input = input("Write phrase: ").strip()
if user_input is not ["", " "]:
    while True:
        # Show all
        if user_chose[0] == "a" or user_chose[0] == str(4):
            all_choice = True

        # How many words
        if user_chose[0] == "w" or user_chose[0] == str(1) or all_choice:
            number = 0
            index = 0
            for x in user_input:
                if user_input[index].lower() in [' ']:
                    number += 1
                index += 1
            print("Your phrase [", user_input, "]. Have", (number + 1), "words.")

        # How many letters
        if user_chose[0] == "l" or user_chose[0] == str(2) or all_choice:
            number = 0
            index = 0
            for x in user_input:
                if user_input[index].lower() in ['a', 'b', 'c', 'd', 'e', 'f', 'g',
                                                 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                                                 'o', 'p', 'q', 'r', 's', 't', 'u',
                                                 'w', 'x', 'y', 'z']:
                    number += 1
                index += 1
            print("Your phrase [", user_input, "]. Have", number, "letters.")

        # How many characters
        if user_chose[0] == "c" or user_chose[0] == str(3) or all_choice:
            print("Your phrase [", user_input, "]. Have", len(user_input), "characters.")
            all_choice = False

        # Change phrase
        if user_chose[0] == "p" or user_chose[0] == str(5):
            user_input = input("Write new phrase: ").strip()

        # Options
        if user_chose[0] == "o" or user_chose[0] == str(6):
            print("""Options:
    1. Number of words in phrase [word] 
    2. Number of letters [letter]
    3. Number of characters [characters]
    4. All information [all]
    5. To change phrase [phrase]
    6. Show options [options]
    7. Show phrase [show]
    8. Quit [quit]""")

        # Show phrase
        if user_chose[0] == "s" or user_chose[0] == str(7):
            print("Your phrase [", user_input, "]")

        # When want to quit
        if user_chose[0] == "q" or user_chose[0] == str(8):
            break

        user_chose = input("type your choice: ")
