import random as r
print("Witaj w grze zgadnij liczbę")

numberOfGuesses = 1
ownSettings = False
bottom_number = 1
top_number = 100

aNumberToGuess = r.randint(bottom_number, top_number)
print("Zgadnij liczbę z przedziału: " + str(bottom_number) + " - " + str(top_number))
while True:
    if ownSettings:
        bottom = input("Podaj najmniejszą liczbę: ")
        top = input("Podaj największą liczbę: ")

        if bottom.isdigit() and top.isdigit() and bottom < top:
            bottom_number = int(bottom)
            top_number = int(top)
            ownSettings = False
            print("Odgadnij liczbę z przedziału: " + str(bottom_number) + " - " + str(top_number))
            aNumberToGuess = r.randint(bottom_number, top_number)
            numberOfGuesses = 0
        else:
            print("błędnie podany zakres ustawienia nie zapisane")
    else:
        theNumberSubmittedByThePlayer = input("Podaj liczbę: ")

        if theNumberSubmittedByThePlayer.isdigit():
            theNumberSubmittedByThePlayer = int(theNumberSubmittedByThePlayer)
            if theNumberSubmittedByThePlayer == aNumberToGuess:
                break
            else:
                if theNumberSubmittedByThePlayer > aNumberToGuess:
                    print("Za dużo")
                elif theNumberSubmittedByThePlayer < aNumberToGuess:
                    print("Za mało")
                numberOfGuesses += 1
        elif theNumberSubmittedByThePlayer == "settings":
            print("jesteś w ustawieniach gry")
            ownSettings = True
        else:
            print("Musisz podać liczbę")

print("Gratulacje wygrana w " + str(numberOfGuesses) + " strzałach")
quit()
