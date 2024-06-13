dim = 500

def setup():
    size(dim,dim)
    rectMode(CENTER)

def draw():
    stroke(random(255),random(255),random(255))
    fill(random(255),random(255),random(255))
    rect(mouseX,mouseY,50,50)
