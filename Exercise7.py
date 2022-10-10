#Healthy Programmer
# 9am - 5pm
# Water - water.mp3 (3.5 litres) - Drank - log - Every 40 min
# Eyes - eyes.mp3 - every 30 min - EyDone - log - Every 30 min
# Physical activity - physical.mp3 every - 45 min - ExDone - log
# Rules
# Pygame module to play audio

from pygame import mixer
from datetime import datetime
from time import time

def music_start(mosic_file,stopper):
      mixer.init()
      mixer.music.load(mosic_file)
      mixer.music.play()
      while(True):
          input_of_user = input()
          if input_of_user == stopper:
              mixer.music.stop()
              break


def typenow(mas):
 with open("prince new.txt",'a') as f:
      f .write(f"{mas} {datetime.now()}\n")

if __name__ == '__main__':
  init_water = time()
  init_eyas = time()
  init_exersice = time()
  water_music_limit = 5
  eyes_music_limit = 10
  exerisice_music_limit = 15

  while (True):
      if time() - init_water > water_music_limit:
          print("This is time for water drinking."
                "if you have drank water Then stop ")
          music_start("D:\\Unstoppable_192(PagalWorld.com.se).mp3",'done')
          init_water = time()
          typenow("done water ")

      if time() - init_eyas > eyes_music_limit:
          print("This is time for eyes exersice. if you have eyes exersice is done then stop "
                )
          music_start("D:\\Unstoppable_192(PagalWorld.com.se).mp3",'done')
          init_eyas = time()
          typenow("done eyes")

      if time() - init_exersice > exerisice_music_limit:
          print("This is time for physical activity. if you have physical activity is done Enter the stop")
          music_start("D:\\Unstoppable_192(PagalWorld.com.se).mp3",'stop')
          init_exersice = time()
          typenow("done exersice")












