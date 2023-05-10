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
        enter_again = simpledialog.askstring("try", "\nDo you want to try again?: ", parent=ws)
        try:
            if enter_again.upper() == "YES" or enter_again.lower() == "y":
                retry = str(enter_again)
                continue
            elif enter_again.upper() == "NO" or enter_again.lower() == "n":
                messagebox.askquestion("CALCULATION ENDED❤", parent=ws)
                time.sleep(3)
                exit()
            else:
                continue    
        except ValueError:
            print("ERROR! Please choose either y or n only.")

while True:
    try:
        num1 = simpledialog.askfloat("input 1", "Enter first number: ", parent=ws)
        num2 = simpledialog.askfloat("input 2", "Enter second number: ", parent=ws)
        operation = simpledialog.askstring("operation", "Enter operation to be use: add, sub, mult, div: ", parent=ws) 

        match operation:
            case "add": 
                result = (num1 + num2)
                messagebox.showinfo("SUM:", result)
                try_again()
                continue               
            case  "sub":
                result = num1 - num2 
                messagebox.showinfo("DIFFERENCE:", result)
                try_again()
                continue
            case "mult" :
                result = (num1 * num2) 
                messagebox.showinfo("PRODUCT:", result)
                try_again()
                continue
            case "div":
                result = (num1 / num2)
                messagebox.showinfo("QUOTIENT:", result)
                try_again()
                continue
            case other:
                messagebox.showinfo("Please choose among the given keyword only")
                continue
      
    except ZeroDivisionError:
        messagebox.showerror("ERROR!! Dividing by zero is not allowed!")
        try_again()
        continue

    except:
        exit()
        
ws.mainloop()
  
            
