from vector import Vector

class Ant:
    def __init__(self,gridx,gridy,xdir,ydir):
        self.gridx = gridx
        self.gridy = gridy
        self.dir = Vector(xdir,ydir)
    
    def rotatecw(self):
        t = -1 * self.dir.x
        self.dir.x=self.dir.y
        self.dir.y = t
    
    def rotateccw(self):
        t = self.dir.x
        self.dir.x = -1 * self.dir.y
        self.dir.y = t
