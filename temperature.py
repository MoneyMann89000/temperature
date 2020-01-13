'''
Date: November 1, 2019
Description: Project 2: Using Python code to build a program that
asks the user for their name, then converts Fahrenheit to Celcius
and vice versa.
Author: Eric Carpenter
'''

# Establishing Constants:
name = input('Enter your name: ')

print('Welcome', name,'to the Temperature Converter Application!')

# Function Definition - Setting Up Main Menu:
def mainMenu():
  print('To convert Fahrenheit to Celcius, enter 1.\n\
  To covert Celcius to Fahrenheit, enter 2.\n\
  Otherwise, to exit the program, exit the program, enter 3.\n\
  \n\
  ')

# Function Definition - Temperatures:
def celcius(tempNum):
    return (tempNum - 32) * 5/9
def fahrenheit(tempNum):
    return tempNum * 9/5 + 32

# Setting Up the Select Ability by using Function Definitions:
def select (temperature, tempNum):
    if temperature == 1:
        celcius(tempNum)
    else:
        fahrenheit(tempNum)

temperature = 0
while temperature != 3:
    mainMenu()
    temperature = int(input('Select a temperature to convert to: '))
    if temperature == 1:
        tempNum = float(input('Enter the temperature in Fahrenheit: '))
        print('The temperature in Celcius is',celcius(tempNum),'° C.')
        print()
    elif temperature == 2:
        tempNum = float(input('Enter the temperature in Celcius: '))
        print('The temperature in Fahrenheit is',fahrenheit(tempNum),'° F.')
        print()
    else:
        print('Exiting program...')
        quit()