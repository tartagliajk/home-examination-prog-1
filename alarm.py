# importerar time modulen, playsound (behövdes installeras med pip), random och os
import time
from playsound import playsound
import random as rand
import os

#hittade denna delen från: https://stackoverflow.com/questions/60250171/how-to-play-random-mp3-files-in-pygame, visste inte hur man skulle göra en path
path = "music/"
mp3file = [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.mp3')]

# definerar funktion alarmklocka
def alarmklocka (t):

    while t:
        mins, sek = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, sek)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    
    print("Time is out, now vibe!")
    #tar en random fil med hjälp av rand choice från random filerna som finns i mapen, sendan spelar den upp den
    randomfile = rand.choice(mp3file)
    playsound(randomfile)
    #öppnar filen och läser den och delar upp den i separata rader
    line = open('poem.txt').read().splitlines()
    #väljer en random rad och printar den
    pickedline =rand.choice(line)
    print(pickedline)

# användare lägger in tid i sekunder
t = input("Enter the time in seconds:\n>")
# öppnar filen som append och läs "mode"
with open("time.txt", "a+") as file:
    #börjar från starten av filen
    file.seek(0)
    #ifall det finns ngt i början av filen så använder den \n
    data=file.read(100)
    if len(data) > 0:
        file.write("\n")
    #lägger till text i slutet av filen
    file.write("Time: {} \(. .)/".format(t))

# kallar på funktion alarmklocka
alarmklocka (int(t))