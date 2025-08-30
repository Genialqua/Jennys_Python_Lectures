'''
We want to build a pizza ordering program with different options of size and flavour
Small_Pizza = 100
Medium_Pizza = 200
Large_Pizza = 300

Pepperoni_small = 30
Pepperoni_medium = 50

Extra_cheese = 20 

First we ask the customer for the type pizza they want and store it in variable called "Pizza"
Then we ask the type of Pepperoni they want and store it in a variable called "Pepperoni"
Lastly we ask if they want extra cheese and store it in a variable called "Cheese"
The we do a summation of their selection and store the result in avariable called "Total"
Then we print the "Total" 

'''
# Prices
Small_Pizza = 100
Medium_Pizza = 200
Large_Pizza = 300
Pepperoni_small = 30
Pepperoni_medium = 50
Cheese = 20

Bill = 0

# Pizza size
pizza_choice = input("What type of pizza do you want? (S/M/L): ").lower()
if pizza_choice == "s":
    Bill += Small_Pizza
elif pizza_choice == "m":
    Bill += Medium_Pizza
else:
    Bill += Large_Pizza

# Pepperoni
pepperoni_choice = input("Do you want pepperoni? (Y/N): ").lower()
if pepperoni_choice == "y":
    if pizza_choice == "s":
        Bill += Pepperoni_small
    else:
        Bill += Pepperoni_medium

# Extra cheese
cheese_choice = input("Do you want cheese? (Y/N): ").lower()
if cheese_choice == "y":
    Bill += Cheese

print(f"Your final bill is {Bill}")