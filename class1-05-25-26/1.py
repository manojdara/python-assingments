#Print your name on the screen
print("Manoj")

#Take input from the user and print welcome message
name = input("Enter your name: ")
print("Welcome, " + name + "!")

#Ask the user for their faviorte food and print a message
food = input("what is your favorite food? ")
print("The " + name + "'s favorite food is " + food)

#Ask the user for their age and print:"You are [age] years old"
age = input("How are old are you? ")
print("You are {} years old".format(age))

#Ask the user for their school or collage name and print a message
School = input("What is your school or collage name? ")
print("The " + name + "'s school or collage name is " + School)

#Take two numbers and print their multiplication result
print("Multiplication of two numbers")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
result = num1 * num2
print("The multiplication of {} and {} is {}".format(num1, num2, result))

#Create a simple calculator that prints addition and subtraction of two numbers
print("Simple Calculator")
def add(x, y):
    """Add two numbers"""
    return x + y

def subtract(x, y):
    """Subtract two numbers"""
    return x - y

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("The addition of {} and {} is {}".format(num1, num2, add(num1, num2)))
print("The subtraction of {} and {} is {}".format(num1, num2, subtract(num1, num2)))

#Ask the user their city name and print:"Hello from [city name]"
city = input("What is your city name? ")
print("Hello from " + city)

#Ask the user:"What AI APP do you want to build?" and print their answer nicely
ai_app = input("What AI APP do you want to build? ")
print("You want to build a " + ai_app + " AI APP")


                                                                    
