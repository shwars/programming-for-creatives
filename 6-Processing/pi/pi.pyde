
dim = 400

ang = 0
pos = 10
                        
def setup():
    global pi
    size(dim, dim)
    background(255)
    colorMode(HSB,10,100,100)
    pi = map(int,loadStrings('pi.txt')[0])
    print(pi)

def draw():
    global pos, ang
    if len(pi)==0:
        return
    s = pi.pop()
    fill(s,100,100)
    stroke(0)
    translate(width/2,height/2)
    rotate(ang)
    ellipseMode(CENTER)
    ellipse(pos,0,10,10)
    pos+=10*10/(2*3.14*pos)
    ang+= 10/pos
    
