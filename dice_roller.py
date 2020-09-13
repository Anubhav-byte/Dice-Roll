import random
def main():
    roll=5
    dice_rolls=int(input("Enter the number of dices you want to roll"))
    dice_side=int(input("How many sides are the dice ?"))
    dice_sum=0
    for i in range(dice_rolls):
        roll=random.randint(1,dice_side)
        dice_sum+=roll
        c_statement=custom_statement(roll)
        print(c_statement)
    print("You have rolled a total of {}".format(dice_sum))


def custom_statement(roll):
    switcher={
    1:"You rolled a {}! Critical failure!".format(roll) ,
    6:"You rolled a {}! Critical Success!".format(roll)

    }
    return switcher.get(roll, "You rolled a {}!".format(roll))
if __name__== "__main__":

    main()
