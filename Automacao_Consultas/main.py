
import time
import pyautogui

# Deverá abrir o navegador e deixar no site onde há os campos (input)

wordlist_matricula = open('extraido.txt', 'r').readlines()
pyautogui.click(x=1033,y=473)
for matricula in wordlist_matricula:
    time.sleep(3)
    pyautogui.write(matricula)   
    time.sleep(10)
    pyautogui.click(x=1033,y=473, clicks=2)
    time.sleep(2)
    pyautogui.press("backspace")
    time.sleep(2)