"""
Ask user for 2  full names "name1" and "name2"
Concatenate the names and store in a variable called "conc_name"
For each letter in the word "true" and "love" get the count in "conc_name"
Then add the total occurence and store in a variable called "Total"
"""

total = 0
total_love = 0
total_true = 0

name1 = input("What is your name? ").lower()
name2 = input("What is your friends name? ").lower()
conc_name = name1 + name2
# print(conc_name)

for ch in "true":
    num = conc_name.count(ch)
    total_true += num


for ch in "love":
    num = conc_name.count(ch)
    total_love += num

total = int(str(total_true) + str(total_love))

if total < 10 or total > 90:
    print(f"Your total is {total}, you go together like coke and mentos")
elif 40 <= total <= 50:
    print(f"Your total is {total}, you are alright together")
else:
    print(f"Your total is {total}.")
