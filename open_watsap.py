import time
from unicodedata import name 
import pyautogui
# time.sleep(8)
# print(pyautogui.position())
def open_wt():
    pyautogui.click(x=794,y=1054)
open_wt()
def send_mss():
    
    
    time.sleep(8)
    pyautogui.click(x=106 ,y=138)
    time.sleep(8)
    pyautogui.write("suraj")
    time.sleep(2)
    pyautogui.click(x=172,y=316)
# a=input("enter the name:")
# b=input("enter the messege:")
    time.sleep(3)
    pyautogui.write("hiii surajjjjj")
    pyautogui.press("Enter")
send_mss()
