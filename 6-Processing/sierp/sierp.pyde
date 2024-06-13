def setup():
    global x,y,verts
    size(400,400)
    x = width / 2
    y = height / 2
    off = 20
    verts = [(off,height-off),(width/2,off),(width-off,height-off)]
    stroke(0)
    strokeWeight(1)
    frameRate(120)
    
def draw():
    global x,y,verts
    n = int(random(3))
    x1,y1 = verts[n]
    x = (x+x1)/2
    y = (y+y1)/2
    point(x,y)
