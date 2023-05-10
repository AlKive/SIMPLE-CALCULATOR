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

def add():
 while True: 
    try:  
            num1 = simpledialog.askinteger("Enter a number: ")
            num2 = simpledialog.askinteger("Enter a second number: ")
     if num1 and num2 is not None:
            
     else:
           print("You don't have a first name?")
            parent=ws,
    except:  
            messagebox.showerror('Error Encountered', 'Error: Please enter a valid input!')
        finally
            
            
