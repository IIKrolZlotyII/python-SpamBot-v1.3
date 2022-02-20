import pyautogui
from time import sleep

print(r"""  
 ________  ________  ________  _____ ______   ________  ________  _________   
|\   ____\|\   __  \|\   __  \|\   _ \  _   \|\   __  \|\   __  \|\___   ___\ 
\ \  \___|\ \  \|\  \ \  \|\  \ \  \\\__\ \  \ \  \|\ /\ \  \|\  \|___ \  \_| 
 \ \_____  \ \   ____\ \   __  \ \  \\|__| \  \ \   __  \ \  \\\  \   \ \  \  
  \|____|\  \ \  \___|\ \  \ \  \ \  \    \ \  \ \  \|\  \ \  \\\  \   \ \  \ 
    ____\_\  \ \__\    \ \__\ \__\ \__\    \ \__\ \_______\ \_______\   \ \__\
   |\_________\|__|     \|__|\|__|\|__|     \|__|\|_______|\|_______|    \|__|
   \|_________|                                                               


 *SpamBot v1.2*
 *Coded by Karol Kaleta*

            """)


#gathering data needed to run code properly 
print("Set the message text")
word = input("")
print("*Massage saved* \n")

print("Set number of messages")
number = int(input())
print("*Number saved* \n")

print("Set the delay betwen messages *Set 0 for no delay*")
delay = int(input())
print("*Delay saved* \n")


#counting down time left for switching tabs
time = 11
while time != 0:
    time -= 1
    sleep(1)
    print("Spammer is waiting... " + str(time))


#main spambot code
count = 0
while count != number:
    sleep(delay)
    count += 1
    print("Send: " + str(count))
    pyautogui.write(word)
    pyautogui.press("enter")

