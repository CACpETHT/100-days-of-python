# #subscripting
# print("Hello"[4])

# #Integer
# print(123 + 345)

# #Large Integer
# print(123_456_789_123_456_789)

# #Float = Floating Point Number
# print(3.14159)

# #boolean
# print(True)
# print(False)

# print(len("Hello"))

# print(type("Hello"))
# print(type(123))
# print(type(3.14159))
# print(type(True))

# name_of_the_user = input("What is your name? ")
# lenght_of_name = len(name_of_the_user)

# print("Number of Letters in your name: " + str(lenght_of_name))

#math operations
# print(3 + 5) #addition
# print(7 - 4) #subtraction
# print(3 * 2) #multiplication
# print(6 / 3) #division
# print(6//3) #floor division
# print(2 ** 3) # 2 to the power of 3

# #PEMDAS
# #What will be the result of this operation?
# print(3 * 3 + 3 / 3 - 3) #PEMDAS

# #change the code so it outputs 3
# print(3 * (3 + 3) / 3 - 3) #PEMDAS

# bmi = 80 / (1.75 * 1.75)
# print(bmi)
# print(int(bmi))
# print(round(bmi,2))

# #score
# score = 0
# height = 1.8
# is_winning = True
# #score = score + 1
# score += 1
# print(score)

# print(f"Your score is {score}, your height is {height}, you are winning is {is_winning}")

#final Test
print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
tip_as_percent = tip / 100
total_tip_amount = total_bill * tip_as_percent
total_bill_with_tip = total_bill + total_tip_amount
bill_per_person = total_bill_with_tip / people
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${final_amount}")