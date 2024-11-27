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
        print("Type 0 or 1. Start over!!!")
        break


    print(f" \n You are a {user_name} trapped in the kitchen. Your goal is to make it through the week without getting tossed in the dumpster. Each day there will be a situation where you can increase or decrease your odds of surviving through the week. 0 will be 'yes', 1 will be 'no'. You start with 3 survival points, dont let them reach 0. Good luck and may the shakers be with you.")


    user_input1 = input("\n The family is having dinner, the food is not hitting, do you shake it on them and do your magic? 0/1?: ")
    if user_input1 == "0":
        survival_points += 1
        print(f"\n Good job! You increased your chances of survival. You currently have {survival_points} survival points.")
    elif user_input1 == "1":
        survival_points -= 1
        print(f"\n Not good! You decreased your chances of survival. You currently have {survival_points} survival points.")
    else:
        print("\n You typed something wrong. Your current location is in the dumpster")
        survival_points -= 10000
        break
    if survival_points <= 0:
        print("\n Your survival points went below 1. You lost. Your current location is now the dumpster. :(")
        break


    user_input2 = input("\n Mom is cooking breakfast, she is making scrambled eggs for the whole family. Do you add your spice to the breakfast? 0/1?: ")
    if user_input2 == "0":
        survival_points += 1
        print(f"\n Good job! You increased your chances of survival. You currently have {survival_points} survival points.")
    elif user_input2 == "1":
        survival_points -= 1
        print(f"\n Not good! You decreased your chances of survival. You currently have {survival_points} survival points.")
    else:
        print("\n You typed something wrong. Your current location is in the dumpster")
        survival_points -= 10000
    if survival_points <= 0:
        print("\n Your survival points went below 1. You lost. Your current location is now the dumpster. :(")
        break


    user_input3 = input(f"\n During family dinner the children are playing and the daughter not so accidentaly knocks you over. You can either hold in your anger or get revenge by shaking up her food with your {user_spice}y emotions. Do you hold it in? 0/1: ")
    if user_input3 == "0":
        survival_points += 1
        print(f"\n Good job! You increased your chances of survival. You currently have {survival_points} survival points.")
    elif user_input3 == "1":
        survival_points -= 1
        print(f"\n Not good! You decreased your chances of survival. You currently have {survival_points} survival points.")
    else:
        print("\n You typed something wrong. Your current location is in the dumpster")
        survival_points -= 10000
    if survival_points <= 0:
        print("\n Your survival points went below 1. You lost. Your current location is now the dumpster. :(")
        break


    user_input4 = input("\n You are feeling tired and beaten. You want to lay down and roll of the table. The breeze of wind would make you feel happy. Do you go skydiving?(skydiving is safe(trust🙏)) 0/1?: ")
    if user_input4 == "1":
        survival_points -= 10000
        print(f"\n You were thinking about the family, but forgot about yourself. You could not take it anymore. You were so so tired, and the boiling hot water tub was looking extra relaxing. You jumped in and mixed with the water, what was once a {user_name} is now just a shaker that lost his meaning.")
    elif user_input4 == "0":
        survival_points -= 1
        print(f"\n Not good! You decreased your chances of survival. You currently have {survival_points} survival points.")
    else:
        print("\n You typed something wrong. Your current location is in the dumpster")
        survival_points -= 10000
    if survival_points <= 0:
        print("\n Your survival points went below 1. You lost. Your current location is now the dumpster. :(")
        break
    


    user_input5 = input("\n The family chose to order food today. You were placed in the cupboard after falling yesterday. You still are a bit dirty. Do you clean yourself up? 0/1?: ")
    if user_input5 == "0":
        survival_points += 1
        print(f"\n Good job! You increased your chances of survival. You currently have {survival_points} survival points.")
    elif user_input5 == "1":
        survival_points -= 1
        print(f"\n Not good! You decreased your chances of survival. You currently have {survival_points} survival points.")
    else:
        print("\n You typed something wrong. Your current location is in the dumpster")
        survival_points -= 10000
    if survival_points <= 0:
        print("\n Your survival points went below 1. You lost. Your current location is now the dumpster. :(")
        break


    user_input6 = input(f"\n The daughter is making dinner tonight. It had to be perfect to impress her grandparents who are coming over. Everything was going well but she forgot about the {user_spice1}. Do you clutch it up for her? (reminder, she knocked you over(now me personally, i wouldnt let that slide)) 0/1?: ")
    if user_input6 == "0":
        survival_points += 1
        print(f"\n Good job! You increased your chances of survival. You currently have {survival_points} survival points.")
    elif user_input6 == "1":
        survival_points -= 1
        print(f"\n Not good! You decreased your chances of survival. You currently have {survival_points} survival points.")
    else:
        print("\n You typed something wrong. Your current location is in the dumpster")
        survival_points -= 10000
    if survival_points <= 0:
        print("\n Your survival points went below 1. You lost. Your current location is now the dumpster. :(")
        break


    if user_input == "0": #salt 
        user_input7_1 = input("\n Today is Sunday, your last day. You have survived this long, you are tired, bruised and just refilled full of salt. You are outraged, this family has put you through hell, but you have to make it. Mom is making the pancake batter but she forgot to add a little bit of salt. Do you add it? 0/1?: ")
        if user_input7_1 == "0":
            user_input7 = input("\n How much do you add? / a pinch / a teaspoon / a tablespoon / THE SALT SHAKER SPECIAL \n 0/1/2/3?: ")
            if user_input7 == "0":
                survival_points += 1
                print(f"\n Good job! You increased your chances of survival. You currently have {survival_points} survival points.")
            elif user_input7 == "1" or user_input7 =="2":
                survival_points -= 1
                print(f"\n Not good! You decreased your chances of survival. You currently have {survival_points} survival points.")
            elif user_input7 == "3":
                print("\n As you shake every last bit of salt that you have left, you look over to the mom's face filled with anger and in the moment, she instantly takes a hold of you and smashes you against the ground. As you are falling to your doom, you think to yourself 'Was this really the right choice?'")
                survival_points -= 10000
        elif user_input7_1 == "1":
            survival_points -= 1
            print(f"\n Not good! You decreased your chances of survival. You currently have {survival_points} survival points.")
        else:
            print("\n You typed something wrong. Your current location is in the dumpster")
            survival_points -= 10000

        if survival_points <= 0:
            print("\n Your survival points went below 1. You lost. Your current location is now the dumpster. :(")
            break
            


    if user_input == "1": #pepper
        user_input7_2 = input("\n Today is Sunday, your last day. You have survived this long, you are tired, bruised and just refilled full of pepper. You are outraged, this family has put you through hell, but you have to make it. Mom is making the pancake batter, she instinctively picks you up but remembers that she is making pancakes. Do you ruin the morning? 0/1?: ")
        if user_input7_2 == "0":
            user_input7 = input("\n How much do you add? / a pinch / a teaspoon / a tablespoon / THE PEPPER SHAKER SPECIAL \n 0/1/2/3?: ")
            if user_input7 == "0":
                survival_points -= 1
                print(f"\n Good job! You increased your chances of survival. You currently have {survival_points} survival points.")
            elif user_input7 == "1" or user_input7 =="2":
                survival_points -= 2
                print(f"\n Not good! You decreased your chances of survival. You currently have {survival_points} survival points.")
            elif user_input7 == "3":
                print("\n As you shake every last bit of pepper that you have left, you look over to the mom's face filled with anger and in the moment, she instantly takes a hold of you and smashes you against the ground. As you are falling to your doom, you think to yourself 'Was this really the right choice?'")
                survival_points -= 10000
        elif user_input7_2 == "1":
            survival_points += 1
            print(f"\n Good job! You increased your chances of survival. You currently have {survival_points} survival points.")
        else:
            print("\n You typed something wrong. Your current location is in the dumpster")
            survival_points -= 10000

        if survival_points <= 0:
            print("\n Your survival points went below 1. You lost. Your current location is now the dumpster. :(")
            break
    print(f"\n Conngratulations, you have made it through one week at the kitchen. You are free to shake anywhere you want, nobody is trying to put you in the garbage. You are finally a free {user_name}. ")
    break