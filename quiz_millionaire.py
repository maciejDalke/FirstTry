import json
import random

print("Welcome in quiz with JSON file!")
question = None
answer = None
score = 0
last_score = None

playing = input("Chcesz zagrać? ").lower()

if playing != "tak" and playing != "yes" and playing != "t" and playing != "y":
    quit("Exit")
else:
    with open("elements\\quiz.json", "r") as json_file:
        data = json.load(json_file)

    # Last_score taken form JSON file
    last_score = data['last_score']
    print("Your last score is: {}".format(last_score))

    # List of questions taken form JSON file
    questions_list = data['questions']

# Questions in order
# for question_index in questions_list:
#     user_input = input("Question {0} \n{1}? :".format(question_index['question_id'] + 1,
#                                                       question_index['question'])).lower()
#     if user_input == question_index['answer']:
#         print("It's correct answer.")
#         score += 1
#     else:
#         print("Incorrect!")

# Question in random order
    random_number_array = []
    while True:
        random_number = random.randint(0, len(questions_list) - 1)
        if random_number not in random_number_array:
            random_number_array.append(random_number)
            user_input = input("   Question {0}/{2} \n{1}? : "
                               .format(len(random_number_array),
                                       questions_list[random_number]['question'],
                                       len(questions_list))).lower()
            if user_input == questions_list[random_number]['answer'] or user_input == "god":
                print("It's correct answer.")
                score += 1
            else:
                print("Incorrect!")
            if len(random_number_array) == len(questions_list):
                break

    # Save new last_score value
    data['last_score'] = score
    with open("elements\\quiz.json", "w") as json_file:
        json.dump(data, json_file)

    print("Your score is {0}/{1}".format(score, len(questions_list)))
