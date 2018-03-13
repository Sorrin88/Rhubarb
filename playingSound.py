from pygame import *

mixer.init()
mixer.music.load("All Star 8 Bit.mp3")  ## - music for 1st level
mixer.music.load("y2mate.com - harder_better_faster_stronger_8_bit_cover_tribute_to_daft_punk_8_bit_universe_1w0gXmE2CuY.mp3")## - music forsecond level
mixer.music.load("Feel Good Inc. [8 Bit Tribute to Gorillaz] - 8 Bit Universe.mp3") ## - music for third level
mixer.music.play()

while mixer.music.get_busy():
    time.Clock().tick(10)




