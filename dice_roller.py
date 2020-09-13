import random
def main():
    roll=5
    dice_rolls=int(input("Enter the number of dices you want to roll"))
    dice_sum=0
    for i in range(dice_rolls):
        roll=random.randint(1,6)
        dice_sum+=roll
        print("You rolled a {}".format(roll))
    print("You have rolled a total of {}".format(dice_sum))
if __name__== "__main__":

    main()
