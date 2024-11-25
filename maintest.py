print("One Week at the Kitchen!👅")
survival_points = 3
while survival_points > 0:
    user_input = input("Would you like to be the salt shaker or the pepper shaker? 0/1?: ")
    if user_input == "0":
        user_name = "Salt shaker"
        user_spice = "salt"
        user_spice1 = "salt"
    elif user_input == "1":
        user_name = "Pepper shaker"
        user_spice = "spic"
        user_spice1 = "pepper"
    else:
        print("Type 0 or 1")

    print(f"You are a {user_name} trapped in the kitchen. Your goal is to make it through the week without getting tossed in the trash. Each day there will be a situation where you can increase or decrease your odds of surviving through the week. 0 will be 'yes', 1 will be 'no'. You start with 3 survival points, do not let them reach 0. Good luck and may the shakers be with you.")


    user_input1 = input("The family is having dinner, the food is not hitting, do you shake it on them and do your magic? 0/1?: ")
    if user_input1 == "0":
        survival_points += 1
        print(f"Good job! You increased your chances of survival. You currently have {survival_points} survival points.")
    elif user_input1 == "1":
        survival_points -= 1
        print(f"Not good! You decreased your chances of survival. You currently have {survival_points} survival points.")
    else:
        print("You typed something wrong. Your current location is in the dumpster")
        survival_points -= 10000
    if survival_points <= 0:
        print("Your survival points went below 1. You lost. Your current location is now the dumpster. :(")
        break