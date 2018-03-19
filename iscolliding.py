    def isColliding(self,player):
        r0 = self.frameWidth/2
        r1 = player.frameWidth/2
        x0 = self.pos.x
        x1 = player.pos.x
        y0 = self.pos.y
        y1 = player.pos.y
        return (r0-r1)*2<=(x0-x1)*2+(y0-y1)*2<=(r0+r1)*2
