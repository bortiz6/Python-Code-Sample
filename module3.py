# Brandon Ortiz
# 10/11/2024
# Assignment 3

# Remember to comment for each function

def print_hello():
    # TODO: Print "Hello World"
    #It is going to show Hello world
    print("Hello World")
    pass

def hello_user(name):
    # TODO: Print "Hello, their_name"
    # This is going to print what is yout name
    name = input("What is your name? ")
    # Then it is going to say hello and the name you chose
    print(f"Hello, {name}")
    pass

def get_circle_area(radius):
    # TODO: print a message back with the answer
    import math
    # It is going to ask you to enter the radius 
    radius = float(input("Please enter the radius of the circle: "))
    # It is going to calculate the area
    area = math.pi * (radius ** 2)
    # It is going to give you the result
    print(f"The area of the circle with radius {radius} is {area:.2f}.")
    pass

def get_miles_per_galoon(miles, gallons):
    # TODO: print out the MPG for the car
    # This is going to ask you to put in a number for the miles driven
    # The same thing is going to happen here but it is gallons used
    miles_driven = float(input("Please enter the number of miles driven: ")) 
    gallons_used = float(input("Please enter the number of gallons used: "))
    # this devides the miles_driven / gallons_used which is going to give you the mpg
    mpg = miles_driven / gallons_used
    # This is going to give the result 
    print(f"The car's fuel efficiency is {mpg:.2f} miles per gallon (MPG).")
    pass
    
def convert_temperature(temperature_F):
    # TODO: return the coverted temperature in Celcius
    # This is going to ask you to enter a number fot the fahranheit
    fahrenheit = float(input("Please enter the temperature in Fahrenheit: "))
    # This is showing that the fahrenheit is being subtracted 
    # Then its being multiplied by five then devided by nine
    # And  by doing that it is going to give you the result in celsius
    celsius = (fahrenheit - 32) * 5 / 9
    # This is going to print out degrees for both fahrenheit and celsius 
    print(f"{fahrenheit} degrees Fahrenheit is equal to {celsius:.2f} degrees Celsius.") 
    pass

def problem_7(starting_day, length_of_stay):
    # TODO: Implement the function as the problem statement
    # This is going to ask you to enter the starting day number and the length of the stay
    starting_day = int(input("Enter the starting day number (0 for Sunday, 6 for Saturday): "))
    nights_stayed = int(input("Enter the number of nights you will be away: "))
    # This is calculating starting_day + nights_stayed % 7 which is going to give you the results for the returning day
    return_day = (starting_day + nights_stayed) % 7
    # This is going to print the results
    print(f"You will return on day number {return_day} of the week.")
    pass

def extra_credit_problem_1():
    start_year = 1900
    end_year = 2100
    # TODO: Write a program to print leap years from the year 1900 to 2100
    # 5 points extra credits
    pass

def extra_credit_problem_2(n):
    # a prime number is a natural number greater than 1, that can only divisible by itself and 1
    # 10 points extra credits
    # TODO: given the number n, check if n is a prime number
    pass


def main():
    print_hello()
    # prompt user to get the input then call functions
    # ...
    
main()


    


