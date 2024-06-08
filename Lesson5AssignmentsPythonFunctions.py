# Lesson 5: Assignments | Python Functions
# Remember to take your time and work through each question diligently! Test your code, make sure it works, and try to find ways to improve. Once you are happy and satisfied with your code, upload it to Github, then turn in your Github link at the bottom of the page!
# Don't forget. Make sure this assignment is in it's own repository. Not mixed in with others!
# ________________________________________
# 1. The Calculator App
# Objective: The aim of this assignment is to build a basic calculator that can perform addition, subtraction, multiplication, and division.

# Task 1: Create functions for each arithmetic operation, with parameters for two numbers to be used in the operation. 
def add(x, y): #This is function of add 
  return x + y

def subtract(x, y): #This is function of subtract
  return x - y

def multiply(x, y):# This is function of multiplies
  return x * y

def divide(x, y):#This is function of divides. It handles division by zero by returning an error message.
    try:
        z = x / y
    except:
        return "Error: Cannot divide by zero."
    else:
        return z
        

# Task 2: Implement user input to receive numbers and an operation choice, their response for operation should call the associated function
while True:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): or enter exit to quit. ")

    # Perform the operation based on the user's choice
    if operation == '+':
        print("Result:", add(num1, num2))
    elif operation == '-':
        print("Result:", subtract(num1, num2))
    elif operation == '*':
        print("Result:", multiply(num1, num2))
    elif operation == '/':
        print("Result:", divide(num1, num2))
    elif operation == 'exit':
        break
    else:
        print("Invalid operation. Please try again.")
# ________________________________________

# 2. The Shopping List Maker
# Objective: The aim of this assignment is to create a program that helps users make a shopping list.

# Task 1: Write a function that lets the user add items to a list, make sure you ask the user what they would like to add (reminder: ensure the function has a parameter to receive the list). Task 2: Include a feature to remove items from the list. Task 3: Add a function that prints out the entire list.


# Task 1: Function to add items to a list
def add_item(my_list):  #Function to add items to a list
    item = input("Enter the item you would like to add: ")
    my_list.append(item)
    print("Item added successfully.")

# Task 2: Function to remove items from a list
def remove_item(my_list): #Function to remove items from a list
    if not my_list:
        print("The list is empty. Nothing to remove.")
    else:
        item = input("Enter the item you would like to remove: ")
        if item in my_list:
            my_list.remove(item)
            print("Item removed successfully.")
        else:
            print("Item not found in the list.")

# Task 3: Function to print the entire list
def print_list(my_list):
    """Function to print the entire list"""
    if not my_list:
        print("The list is empty.")
    else:
        print("Items in the list:")
        for item in my_list:
            print(item)

# shopping cart usage
my_list = []

while True:
    print("\nOptions:")
    print("1. Add an item to the list")
    print("2. Remove an item from the list")
    print("3. Print the entire list")
    print("4. Exit")

    choice = input("Enter your choice (1, 2, 3, or 4): ")

    if choice == '1':
        add_item(my_list)
    elif choice == '2':
        remove_item(my_list)
    elif choice == '3':
        print_list(my_list)
    elif choice == '4':
        print("Exiting the shopping")
        break
    else:
        print("Invalid choice. Please enter a valid option (1, 2, 3, or 4).")