class Turtle:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.angle = 0  # Angle in degrees

    def forward(self, distance):
        # Calculate new position
        new_x = self.x + cos(radians(self.angle)) * distance
        new_y = self.y + sin(radians(self.angle)) * distance
        # Draw line to new position
        line(self.x, self.y, new_x, new_y)
        # Update position
        self.x = new_x
        self.y = new_y

    def left(self, angle):
        # Increase the angle (turn left)
        self.angle -= angle

    def right(self, angle):
        # Decrease the angle (turn right)
        self.angle += angle

dim = 400

turtle = None
l = 200

# Закомментируйте одну или другую грамматику, чтобы увидеть разные фигуры

# angle = 120
# grammar = { 'F' : 'F-G+F+G-F', 'G' : 'GG' }
# s = 'F-G-G'

angle = 60
grammar = { 'F' : 'G-F-G', 'G' : 'F+G+F' }
s = 'F'

def expand(s):
    return ''.join([ grammar.get(x,x) for x in s])

def plot(l,s):
    for x in s:
        if x == 'F' or x == 'G':
            turtle.forward(l)
        elif x == '+':
            turtle.right(angle)
        elif x == '-':
            turtle.left(angle)
        else:
            pass
            
def setup():
    size(dim, dim)
    frameRate(1)
    background(255)

def draw():
    global turtle,s,l
    background(255)
    turtle = Turtle(10, height / 2)    
    plot(l,s)
    s = expand(s)
    print(s)
    l /= 2
