#ramdom module
import random
# random_integer = random.randint(1, 10)
# print(random_integer)

# random_float = random.random()
# print(random_float)

# #head or tail
# print(input("Welcome to the coin toss simulator!, Press enter to toss the coin."))

# random_side = random.randint(0, 1)
# if random_side == 1:
#     print("Heads")
# else:
#     print("Tails")

#list
# states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana","Washington","Idaho","Wyoming","Utah","Oklahoma","New Mexico","Arizona","Alaska","Hawaii"]
# print(states_of_america[random.randint(0, len(states_of_america) - 1)])

# friends = ["Rolf", "Bob", "Jen", "Anne"]
# # print(friends[random.randint(0, len(friends) - 1)])
# print(random.choice(friends))

#dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]
# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes"]
# vegetables = ["Spinach", "Kale", "Celery", "Potatoes"]

# dirty_dozen = [fruits, vegetables]
# print(dirty_dozen[1][2]) #the first index is for the list of vegetables and the second index is for the item in the vegetable list, which is celery.

option = ["rock", "paper", "scissors"]
user_choice = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors.\n"))
computer_choice = random.randint(0, 2)
print(f"You chose {option[user_choice]}")
print(f"Computer chose {option[computer_choice]}")
if user_choice == computer_choice:
    print("It's a draw.")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif user_choice == 1 and computer_choice == 0:
    print("You win!")
elif user_choice == 2 and computer_choice == 1:
    print("You win!")
else:    
    print("You lose.")