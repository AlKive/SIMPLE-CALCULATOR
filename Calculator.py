# BABIERA,ALEXA | CMPE-103-MODULE-2-FILE-HANDLING-IN PYTHON | PROGRAMMING EXERCISE 4
'''This program asks the user for input (integers) and calculate them using 
 user's choice of mathematical operation such as addition, subtraction, multiplication 
 and division. This program also exhibits exceptionhandling or catching errors using 
 appropriate exceptions.'''
 
from pyfiglet import figlet_format
from termcolor import colored
from colorama import Back, Fore, Style, init
import time

from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox
ws = Tk()
ws.title("SIMPLE CALCULATOR")
ws.geometry('400x300')
ws.config(bg='#4a7a8c')

def try_again():
    retry = None
    while retry is None:
        again = input("\nDo you want to try again (y/n)? ")
        try:
            if again.lower() == "y":
                retry = str(again)
                continue
            elif again.lower() == "n":
                exit("\nTHANK YOU FOR USING MY PROGRAM! ❤")
            else:
                print("ERROR! Please choose either y or n only.")
        except ValueError:
            print("ERROR! Please choose either y or n only.")

while True:
    try:
        num1 = simpledialog.askinteger("input 1", "Enter first number: ", parent=ws)
        num2 = simpledialog.askinteger("input 2", "Enter second number: ", parent=ws)
        operation = simpledialog.askstring("operation", "Enter operation to be use: add, sub, mult, div: ", parent=ws) 

        match operation:
            case "add": 
              result = (num1 + num2)
              messagebox.showinfo("Result:", result)
            
            case  "sub":
              result = num1 - num2 
              messagebox.showinfo("Result:", result)

            case "mult" :
                result = (num1 * num2) 
                messagebox.showinfo("Result:", result)

            case "div":
                result = (num1 / num2)
                messagebox.showinfo("Result:", result)

            case other:
                messagebox.showinfo("Please choose among the given keyword only")
        try_again()

    except ZeroDivisionError:
        print("ERROR!! Dividing by zero is not allowed!")
        try_again()

    except:
        print("Invalid Input! Please enter a valid input!")
        try_again()
        
    ws.mainloop()
            
