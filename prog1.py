# Program Author: Regan Setter
# Student ID number: 3505894
# Program one - Six Math Functions
# February 4th, 2021

# A program written in Python that allows you to perform six different mathematics functions between two numbers

# Define add

def add(x, y):
    return x + y


# Define subtract

def subtract(x, y):
    return x - y


# Define multiply

def multiply(x, y):
    return x * y


# Define divide

def divide(x, y):
    return x / y


# Define exp

def exp(x, y):
    return x ** y


# Define mod

def mod(x, y):
    return x % y


# Print out the options for the user to choose from

print("Select one of the operations that you wish to perform.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Exponent")
print("6. Remainder")

# Tell the user they only have options 1 through 6 to choose from

choice = input("Enter your choice from 1-6:")

# Tell the user to input their first and second numbers for the mathematics problem

num1 = int(input("Please enter your first number: "))
num2 = int(input("Please enter your second number: "))

# If you choose number one, print out num1 + num2 =

if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))

# If you choose number two, print out num1 - num2 =

elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))

# If you choose number three, print out num1 * num2 =

elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))

# If you choose number four, print out num1 / num2 =

elif choice == '4':
    print(num1, "/", num2, "=", divide(num1, num2))

# If you choose number five, print out num1 ** num2 =

elif choice == '5':
    print(num1, "**", num2, "=", exp(num1, num2))

# If you choose number six, print out num1 % num2 =

elif choice == '6':
    print(num1, "%", num2, "=", mod(num1, num2))

# Otherwise, if you input any other value that isn't between 1 and 6, print Invalid input

else:
    print("Invalid input")
