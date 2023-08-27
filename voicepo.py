import speech_recognition as sr
import webbrowser
import random
import pygame.mixer
import time


recording = sr.Recognizer()
pygame.mixer.init()

pygame.mixer.music.load('main.mp3')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
     time.sleep(1)
with sr.Microphone() as source:
    recording.adjust_for_ambient_noise(source)
    print("ROCK PAPER SCISSORS")
    audio = recording.listen(source)


user_input = recording.recognize_google(audio)
print("said",user_input)

game = ['rock','paper','scissors']
r =random.choice(game)
print("COMPUTER=",r)
print("PLAYER =",user_input)

if  ( (r=="paper" and user_input=="rock") or(r=="scissors" and user_input=="paper") or (r=="rock" and user_input=="scissors") ):
    print("COMPUTER WON\n")
    pygame.mixer.music.load('lost.mp3')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
     time.sleep(1)
elif  ( (user_input=="paper" and r=="rock") or(user_input=="scissors" and r=="paper") or (user_input=="rock" and r=="scissors") ):
    print("YOU WON\n")
    pygame.mixer.music.load('won.mp3')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
     time.sleep(1)
else:
    print("TIE")