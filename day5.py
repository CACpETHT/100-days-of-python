import random
# #for loop
# fruits = ["Apple", "Peach", "Pear"]

# for fruit in fruits:
#     print(fruit)

#Get higest students score
# students_score = [96,85,97,64,50]

# # print(max(students_score))

# max_score = 0
# for student_score in students_score:
#     if student_score > max_score:
#         max_score = student_score

# print(max_score)

# #Gauss Challenge
# total = 0
# for number in range(1,101):
#    total += number

# print(total)
    
#Password Generator
letters = ["a", "b", "c", "d", "e"]
numbers = ['0','1','2','3','4']
symbols = ['!', '@', '#', '%']

print(input("welcome to the PyPassword Generator!, Press enter to continue"))
nr_letters = int(input("How Many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like? \n"))
nr_number = int(input(f"How Many numbers would you like?\n"))


# option = ["rock", "paper", "scissors"]
# computer_choice = random.randint(0, 2)
# print(f"You chose {option[user_choice]}")

# #Easy Way

# password = ""
# for letter in range(1,nr_letters + 1):
#     # random_letter = random.randint(0,len(letters) -1)
#     # password += letters[random_letter]
#     # ran_letter = random.choice(letters)
#     # password += ran_letter
#     password += random.choice(letters)


# for symbol in range(1,nr_symbols + 1):
#     # random_symbol = random.randint(0,len(symbols) -1)
#     # password += symbols[random_symbol]
#     # ran_symbol = random.choice(symbols)
#     # password += ran_symbol
#     password += random.choice(symbols)

# for number in range(1,nr_number + 1):
#     # random_number = random.randint(0,len(numbers) -1)
#     # password += numbers[random_number]
#     # ran_number = random.choice(numbers)
#     # password += ran_number
#     password += random.choice(numbers)


# print(password)

#hard Way

# password = ""
password_list = []
for letter in range(1,nr_letters + 1):
    password_list.append(random.choice(letters))


for symbol in range(1,nr_symbols + 1):
    password_list.append(random.choice(symbols))

for number in range(1,nr_number + 1):
    password_list.append(random.choice(numbers))


random.shuffle(password_list)
#print(password_list)
password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")