dim = 500

def setup():
    size(dim,dim)
    rectMode(CORNERS)
    smooth()

a = 0

def draw():
    global a
    translate(dim/2,dim/2)
    rotate(radians(a))
    a+=1
    stroke(random(255),random(255),random(255))
    fill(random(255),random(255),random(255),128)
    rect(random(dim),random(dim),random(dim),random(dim))
