from ast import Num
import os
from time import time
from tkinter import Button
import pyautogui as ok
import pyautogui
import keyboard
import time
r = r"C:\Users\hp\Desktop\New folder"
read_file = open("pass.txt", 'r')
readpass = read_file.read()


if readpass == "":

    # a = ok.confirm("do you want set password",buttons=["yes","no"])

    # if a == "yes":
    None == " "
    c = ok.prompt("set the password")
    
    d = open("pass.txt", 'w')

    d.write(c)


# print(b)
else:
    i = 0
    while i < 3:

        b = ok.password("enter the password")
        time.sleep(7)
        
        
        e = open("pass.txt", 'r')
        p = e.read()
        if b == p:
            
            import tur

            resett = pyautogui.confirm(
                "do you want reset password", buttons=["yes", "no"])
                
            if resett == "yes":
                from make_file_empty import empty
                empty()
                break
            else:
                pass

        else:
            ok.alert("you have enterd wrong password")

        i = i+1
