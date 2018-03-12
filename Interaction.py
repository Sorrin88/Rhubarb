from Platform2 import *
class Interaction:
    def __init__(self, object,platform):
        self.object = object
        self.platform = platform
        self.inCollision = False

    def update(self):
        if (self.platform.distanceTo(self.object.pos) < self.platform.thickness + self.object.radius and
            self.platform.collide(self.object.pos)):
            if not self.inCollision:
                self.object.stop(self.platform.normal)
                self.inCollision = True
        else:
            self.inCollision = False