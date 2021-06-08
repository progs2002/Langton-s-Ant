class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __repr__(self):
        return str(self.x) +"i, "+ str(self.y)+"j"

def dotProduct(v1,v2):
    return v1.x*v2.x + v1.y*v2.y