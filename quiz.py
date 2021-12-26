print("Witam w quizie!")

playing = input("Chcesz zagrać? ").lower()

if playing != "tak" and playing != "yes" and playing != "t" and playing != "y":
    quit("Exit")

name = input("Podaj imię: ")
score = 0

answer = input("Co to CPU? ").lower()
if answer == "central processing unit":
    print("Poprawna odpowiedź")
    score += 1
else:
    print('Błędna odpowiedź')

answer = input("Co to GPU? ").lower()
if answer == "graphic processing unit":
    print("Poprawna odpowiedź")
    score += 1
else:
    print('Błędna odpowiedź')

answer = input("Co to RAM? ").lower()
if answer == "random access memory":
    print("Poprawna odpowiedź")
    score += 1
else:
    print('Błędna odpowiedź')

answer = input("Co to PSU? ").lower()
if answer == "power supply":
    print("Poprawna odpowiedź")
    score += 1
else:
    print('Błędna odpowiedź')

print(name + " zdobył/a " + str(score) + "/4 that is " + str((score/4)*100) + "%")
