import time
import pyautogui
import pyautogui as gp
from keyboard import press_and_release
from aii import takeCommand
import keyboard
# time.sleep(8)
# print(pyautogui.position())
def scan():#for scan the system

    # pyautogui.click(x=1318,y=1045)
    # # time.sleep(1)
    # pyautogui.click(x=595,y=417)
    # # time.sleep(1)
    # pyautogui.click(x=1300,y=515)
    keyboard.press_and_release('windows+r')
    gp.write("mrt")
    gp.press('Enter')
    # gp.press('Enter')
    time.sleep(8)
    # keyboard.press('Left arrow')
    gp.press("Enter")
    gp.press("Enter")


def stop_scan():#stop the scaning systemmrt

    pyautogui.click(x=1310,y=708)
    pyautogui.click(x=909,y=555)
    
# def mini_all():
#     pyautogui.click(x=1919,y=1079)

# mini_all()
# scan()
# # for i in range(5):
# keyboard.press('fn')
# keyboard.press('f7')
# keyboard.release('f7')
# keyboard.release('fn')

def open_booksmarks_bar():#for openingboobkmarks bar
    keyboard.press_and_release("Ctrl + Shift + b")
# open_booksmarks_bar()
scan()