from pygame import *

mixer.init()
mixer.music.load("All Star 8 Bit.mp3")  ## - music for 1st level
mixer.music.load("harder_better_faster_stronger.mp3")## - music forsecond level
mixer.music.load("Feel Good Inc. [8 Bit Tribute to Gorillaz] - 8 Bit Universe.mp3") ## - music for third level
mixer.music.play()

while mixer.music.get_busy():
    time.Clock().tick(10)




