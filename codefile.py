import pygame
from pygame import mixer
from time import time
from datetime import datetime
pygame.mixer.init()

def musiconloop(file):

    mixer.music.load(file)
    mixer.music.set_volume(9)
    mixer.music.play(-1)
    a=input("IS IT DONE ? Write Y/N :")
    if a=='Y' :
        mixer.music.stop()
    else :
        print("Do it Fast")
        musiconloop(file)


def log_Now(msg):
    with open("Mylog.txt","a") as f1:
        f1.write(f"{msg} {datetime.now()}\n")


if __name__ == '__main__':
    initial_water=time()
    initial_eye=time()
    initial_exercise=time()

    water_Second=1*60
    eye_second=1.5*60
    exercise_second=2*60

    while True:
        if time()-initial_water>water_Second:
            print("This is The Water Breake...")
            musiconloop("sukalyan-drink-the-water.mp3")
            initial_water=time()
            log_Now("I have drunk the water ")
            a=input(("Do you want to terminate :"))
            if a=='Y':
                break

        elif time()-initial_eye>eye_second:
            print("This is The Eye Breake Time...")
            musiconloop("sukalyan-eye-exercise-time.mp3")
            initial_eye=time()
            log_Now("I have taken the eye breake ")
            b = input(("Do you want to terminate :"))
            if b == 'Y':
                break

        elif time()-initial_exercise>exercise_second:
            print("This is the exercise time...")
            musiconloop("sukalyan-exercise-time.mp3")
            initial_exercise=time()
            log_Now("I have taken the exercise breake ")
            c = input(("Do you want to terminate :"))
            if c == 'Y':
                break
