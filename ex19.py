# Creates a function called "cheese_and_crackers" with to arguments,
# "cheese_count" and "boxes_of_crackers"
def cheese_and_crackers(cheese_count, boxes_of_crackers):
# prints the value of "cheese_count" in a string using digit formatter
    print(f"You have {cheese_count} cheeses!")
# prints the value of "boxes_of_crackers" in a string using digit formatter
    print(f"You have {boxes_of_crackers} boxes of crackers!")
# prints a string
    print("Man that's enough for a party!")
# prints a string
    print("Get a blanket.\n")

# prints a string
print("We can just give the function numbers directly:")
# calls the function "cheese_and_crackers" with argument value of 20 and 30
cheese_and_crackers(20,30)

# prints a string
print("OR, we can use variables from our script:")
# creates variable "amount_of_cheese" with value "10"
amount_of_cheese = 10
# creates variable "amount_of_crackers" with value "50"
amount_of_crackers = 50
# call the function "cheese_and_crackers" with arguments set to the variables
# "amount_of_cheese" and "amount_of_crackers", whose values respectively are 
# set to "10" and "50".
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# prints a string
print("We can even do math inside too:")
# calls the function "cheese_and_crackers" with the arguments "10+20" and "5+6"
# which proves it's possible to do math on the arguments/values passed to the 
# function
cheese_and_crackers(10+20, 5+6)

# prints a string
print("And we can combine the two, variables and math:")
# calls the function "cheese_and_crackers" with the arguments 
# "amount_of_cheeses+100" and "amount_of_crackers +1000" which proves it's 
# possible to do math on the variables passed to the function
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)