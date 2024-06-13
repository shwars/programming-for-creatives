dim = 500

class Ball:
    def __init__(self,radius=10):
        self.x = random(dim)
        self.y = random(dim)
        self.cfill = (random(255),random(255),random(255))
        self.cstroke = (0,0,0)
        self.dx = random(3)-1
        self.dy = random(3)-1
        self.radius = radius

    def show(self):
        stroke(*self.cstroke)
        fill(*self.cfill)
        ellipse(self.x,self.y,self.radius,self.radius)
        
    def update(self):
        self.x += self.dx
        self.y += self.dy
        if self.x-self.radius<=0 or self.x+self.radius>=dim:
            self.dx = -self.dx
        if self.y-self.radius<=0 or self.y+self.radius>=dim:
            self.dy = -self.dy
        
objs = []

def setup():
    size(dim,dim)
    ellipseMode(CENTER)
    for i in range(100):
        objs.append(Ball())
    smooth()

def draw():
    background(255)
    for o in objs:
        o.show()
        o.update()
