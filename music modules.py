# from playsound import playsound
# playsound("D:\\Unstoppable_192(PagalWorld.com.se).mp3")


import pygame
import time

def sum ():
    x = int(input("Enter the value a "))
    y = int(input("Enter the value b "))
    z = x+y
    print("sum",z)
def play_audio():
  pygame.init()
  file = "D:\\Unstoppable_192(PagalWorld.com.se).mp3"
  pygame.mixer.music.load(file)
  pygame.mixer.music.play()

sum()
time.sleep(12)
play_audio()
x = input(" you con stop the music then s enter ")
if x == "s":
 pygame.mixer.music.stop()
 print("Good Bye")


print("Good Bye")


