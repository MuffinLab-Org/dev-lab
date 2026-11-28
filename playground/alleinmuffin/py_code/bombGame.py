import random
def print_the_range(lower_limit, upper_limit):
    print(f"The bomb number is in the range ({lower_limit}, {upper_limit}).")
def judge_the_bomb(bomb_number):
    global lower_limit, upper_limit
    while True:
        try:
            chosen_number = int(input("Choose a number within the range: "))
            if chosen_number <= lower_limit or chosen_number >= upper_limit:
                    print(f"The chosen number must be within the range of ({lower_limit}, {upper_limit}). Please try again.")
                    continue
            if chosen_number == bomb_number:
                print("You have hit the bomb! GAME OVER!")
                break
            else:
                print("You have not hit the bomb. Keep playing.")
                if chosen_number < bomb_number:
                    lower_limit = chosen_number
                    print_the_range(lower_limit, upper_limit) 
                    continue
                else:
                    upper_limit = chosen_number
                    print_the_range(lower_limit, upper_limit)
                    continue
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue
try:
    lower_limit = int(input("Choose a number for a lower limit: "))
    upper_limit = int(input("Choose a number for an upper limit: "))
except ValueError:
    print("Invalid input. Please enter valid integers for the limits.")
    exit(1)
if upper_limit - lower_limit < 3:
    print("The difference between the upper and lower limits must be at least 3. Please try again.")
    exit(1)
print(f"You have selected the range of ({lower_limit}, {upper_limit})")
bomb_number = random.randint(lower_limit+1, upper_limit-1)
print("Bomb has been planted! you will choose a number within that range.GAME STARTS!")
judge_the_bomb(bomb_number)

