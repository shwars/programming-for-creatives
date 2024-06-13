dim = 800 

def setup():
    global tx,ty,th
    size(dim, dim)
    tx = width/2
    ty = height/2
    th = 0
    background(255)
    
def forward(amount):
    global tx,ty,th
    newX = tx + cos(radians(th)) * amount
    newY = ty + sin(radians(th)) * amount
    line(tx, ty, newX, newY)
    fill(0)
    tx = newX
    ty = newY
    
def right(degrees):
    global th
    th += degrees

def left(degrees):
    right(-degrees)

def draw():
    stroke(random(256), random(256), random(256))
    right(random(360))
    length = random(0, 150)
    
    forward(length)
    right(90)
    
    forward(length)
    right(90)
    
    forward(length)
    right(90)
    forward(length)
    
