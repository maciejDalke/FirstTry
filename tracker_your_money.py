import json

print("Wydatki")

person_id = 0
name = ""
second_name = ""
last_name = ""
birth_year = None
phone_number = None
persons = []

while True:
    person_id += 1
    name = input("Podaj imię: ")
    second_name = input("Podaj drugie imię: ")
    last_name = input("Podaj nazwisko: ")
    birth_year = input("Podaj rok urodzenia: ")
    phone_number = input("Podaj numer telefonu: ")
    temp = input("Zapisać w pliku: ")
    if temp == "tak":
        persons.append({"person_id": person_id,
                        "name": name,
                        "second_name": second_name,
                        "last_name": last_name,
                        "birth_year": birth_year,
                        "phone_number": phone_number})
    else:
        break

print("yolo")


print(persons)

variable_one = 'dupa'
variable_two = 'pupa'
string_variable = 'Longer string for test.'
integer_variable = 123456789

dictionary = {'persons': persons,
              'variable_one': variable_one,
              'variable_two': variable_two,
              'string_variable': string_variable,
              'integer_variable': integer_variable
              }

# Serializing json
json_object = json.dumps(dictionary, indent=4)

# Writing to file
with open("elements\\money.json", "w") as outfile:
    outfile.write(json_object)
    # json.dump(json_object, outfile)
