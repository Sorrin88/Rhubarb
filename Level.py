try:
    import simplegui
except:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from Platfrom2 import Platform2
from Interaction import Interaction
from Vector import Vector
from Player import  Player
from Monster import Monster
from ChickenMonster2 import ChickenMonster2
from PlatformItem import PlatformItem
from SpeedUpItem import SpeedUpItem
from JumpUpItem import JumpUpItem
from InvincibleItem import InvincibleItem
from LifeUpItem import LifeUpItem
from FireTrap import FireTrap
from FinishLine import FinishLine
from HelicopterFinishLine import HelicopterFinishLine
from PortalFinishLine import PortalFinishLine
from Flood import Flood

from LevelBackground import LevelBackground

class Level:

    def __init__(self, player, goatNumber, chickenNumber, platformItems, finishLine, backgroundImage):

        self.backgroundImage = simplegui.load_image(backgroundImage)
        #^
        #lv1 https://i.imgur.com/Q7tBgIc.png
        #lv2 https://i.imgur.com/QdnOKPM.png
        #lv3 https://i.imgur.com/15DHBtk.png
