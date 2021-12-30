import random as r

ownSettings = False

# listy
options = ["rock", "paper", "scissors", "lizard", "spock"]
options_computer = ["rock", "paper", "scissors", "lizard", "spock", "scissors"]

# punktacja
player_points = 0
computer_points = 0
draws = 0

# opcje programu
points_to_win = 5
advantage_enable = False
advantage_to_win = 2

while True:
    user_input = input("Twój wybór: ").lower()

    if user_input == "q" or user_input == "quit":
        print("Current Score P[{0}] C[{1}] /{2}"
              .format(player_points, computer_points, player_points + computer_points + draws))
        quit("quit elo")

    elif user_input == "setup":
        setting = input("Now game is to win {} rounds. Change to best of [if you don't want change leave blanked]: "
                        .format(points_to_win))
        if setting.isdigit() and int(setting) > 0:
            points_to_win = int(setting)
            print("new number of wins needed [{}]".format(points_to_win))

        setting = input("Advantage is now [{0}] want change? [yes] or [y]: "
                        .format(advantage_enable and "enable" or "disable")).lower()
        if setting[0] == "y":
            advantage_enable = not advantage_enable
            print("advantage is [{}]".format(advantage_enable and "enable" or "disable"))

        ownSettings = True

    elif user_input not in options:
        print("""
    Nie można tego zinterpretować wybierz jedno z:
    {0} 
                                 Quit lub q aby wyjść 
        """.format(options))
        continue

    else:
        randomly_selected_for_a_computer = options_computer[r.randint(0, 5)]
        options_computer[5] = randomly_selected_for_a_computer

        # rock: 0
        if user_input == options[0]:
            if randomly_selected_for_a_computer == "rock":
                print("It's draw. Two rocks make sparks")
                draws += 1
            elif randomly_selected_for_a_computer == "paper":
                print("You lost. Rock was covered by Paper")
                computer_points += 1
            elif randomly_selected_for_a_computer == "scissors":
                print("You win! Rock crushes Scissors")
                player_points += 1
            elif randomly_selected_for_a_computer == "lizard":
                print("You win! Rock crushes Lizard")
                player_points += 1
            elif randomly_selected_for_a_computer == "spock":
                print("You lost. Rock was vaporized by Spock")
                computer_points += 1

        # paper: 1
        elif user_input == options[1]:
            if randomly_selected_for_a_computer == "rock":
                print("You win! Paper covers Rock")
                player_points += 1
            elif randomly_selected_for_a_computer == "paper":
                print("It's draw.")
                draws += 1
            elif randomly_selected_for_a_computer == "scissors":
                print("You lost. Paper was cut by Scissors")
                computer_points += 1
            elif randomly_selected_for_a_computer == "lizard":
                print("You Lost. Paper was eaten by a Lizard")
                computer_points += 1
            elif randomly_selected_for_a_computer == "spock":
                print("You Win! Paper disproves Spock")
                player_points += 1

        # scissors: 2
        elif user_input == options[2]:
            if randomly_selected_for_a_computer == "rock":
                print("You lost. Scissors were destroyed by Rock")
                computer_points += 1
            elif randomly_selected_for_a_computer == "paper":
                print("You win! Scissors cuts Paper")
                player_points += 1
            elif randomly_selected_for_a_computer == "scissors":
                print("It's draw! They scissor themselves")
                draws += 1
            elif randomly_selected_for_a_computer == "lizard":
                print("You win! Scissors decapitates Lizard")
                player_points += 1
            elif randomly_selected_for_a_computer == "spock":
                print("You lost. Scissors were smashes by Spock")
                computer_points += 1

        # lizard 3
        elif user_input == options[3]:
            if randomly_selected_for_a_computer == "rock":
                print("You lost. Lizard has been crushes by a Rock")
                computer_points += 1
            elif randomly_selected_for_a_computer == "paper":
                print("You win! Lizard eats Paper")
                player_points += 1
            elif randomly_selected_for_a_computer == "scissors":
                print("You lost. Lizard has been decapitated by a Scissors")
                computer_points += 1
            elif randomly_selected_for_a_computer == "lizard":
                print("It's draw! Lizards went to make babies ;D")
                draws += 1
            elif randomly_selected_for_a_computer == "spock":
                print("You win! Lizard poisons Spock")
                player_points += 1

        # spock 4
        elif user_input == options[4]:
            if randomly_selected_for_a_computer == "rock":
                print("You win! Spock vaporized Rock")
                player_points += 1
            elif randomly_selected_for_a_computer == "paper":
                print("You lost. Spock was disproved by Paper")
                computer_points += 1
            elif randomly_selected_for_a_computer == "scissors":
                print("You win! Spock smashed Scissors")
                player_points += 1
            elif randomly_selected_for_a_computer == "lizard":
                print("You lost. Spock was poisoned by Lizard")
                computer_points += 1
            elif randomly_selected_for_a_computer == "spock":
                print("You almost lost but it's draw. There's only one Spock!!!")
                draws += 1

    if ownSettings:
        player_points = 0
        computer_points = 0
        draws = 0
        ownSettings = not ownSettings

    print("""P[{0}] C[{1}] 
    """.format(player_points, computer_points))

    if player_points == points_to_win and \
            (advantage_enable and (computer_points + advantage_to_win <= player_points) or True):
        print("""
    Player win! 
        Congratulation!!! 
    Score is {} - {} with {} draws"""
              .format(player_points, computer_points, draws))
        break
    elif computer_points == points_to_win and \
            (advantage_enable and (player_points + advantage_to_win <= computer_points) or True):
        print("""
            You lost! 
                Shame!!! 
            Score is {} - {} with {} draws"""
              .format(player_points, computer_points, draws))
        break
    else:
        continue
