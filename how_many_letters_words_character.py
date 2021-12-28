print("How many letters/words/characters... in phrase program")
all_choice = False
vowel_list = ['a', 'e', 'i', 'o', 'u', 'y',
              'ą', 'ę', 'ó']
consonant_list = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'r', 's', 't', 'w', 'y', 'z',
                  'ć', 'ż', 'ź']
number_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
punctuation_symbols_list = ['!', '@', '<', '>', ',', '.', '?', ':', ';', "'", '"']
brackets_list = ['[', ']', '{', '}', '(', ')']
symbols_list = ['@', '#', '$', '%', '^', '&', '*', '-', '_', '+', '=', '|', '/']
# Ala ma kota. Kot ma Ale w dupie!

# TODO: Dodanie możliwości wczytywania ciągu z pliku

# simple one with writing string
user_chose = "o"
user_input = input("Write phrase: ").strip()
if user_input is not ["", " "]:
    while True:
        # TODO: wyrażenia regularne / zmiana input / liczenie samogłosek czy spółgłosek

        # Show phrase
        if user_chose[0] == "s" or user_chose[0] == str(0):
            print("Your phrase [", user_input, "]")

        # Show all
        if user_chose[0] == "a" or user_chose[0] == str(5):
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
                if user_input[index].lower() in vowel_list or user_input[index].lower() in consonant_list:
                    number += 1
                index += 1
            print("Your phrase have", number, "letters.")

        # How many characters
        if user_chose[0] == "c" or user_chose[0] == str(3) or all_choice:
            print("Your phrase have", len(user_input), "characters.")

        # How many vowel and consonant
        if user_chose[0] == "v" or user_chose[0] == str(4) or all_choice:

            vowel_number = 0
            consonant_number = 0
            index = 0
            for x in user_input:
                if user_input[index].lower() in vowel_list:
                    vowel_number += 1
                elif user_input[index].lower() in consonant_list:
                    consonant_number += 1
                index += 1
            print("Your phrase have", vowel_number, "vowels and", consonant_number, "consonants")
            all_choice = False

        # Change phrase
        if user_chose[0] == "p" or user_chose[0] == str(6):
            user_input = input("Write new phrase: ").strip()

        # Options
        if user_chose[0] == "o" or user_chose[0] == str(7):
            print("""Options:
    0. Show phrase [show]
    1. Number of words in phrase [word] 
    2. Number of letters [letter]
    3. Number of characters [characters]
    4. Number of vowel and consonant [vowel]
    5. All information [all]
    6. To change phrase [phrase]
    7. Show options [options]
    9. Quit [quit]""")

        # When want to quit
        if user_chose[0] == "q" or user_chose[0] == str(9):
            break

        user_chose = input("type your choice: ")
