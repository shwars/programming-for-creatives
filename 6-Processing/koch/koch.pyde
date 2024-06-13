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

def mink(n,x):
    if n==1:
        turtle.forward(x)
    else:
        mink(n-1,x/4)
        turtle.left(90)
        mink(n-1,x/4)
        turtle.right(90)
        mink(n-1,x/4)
        turtle.right(90)
        mink(n-1,x/4)
        mink(n-1,x/4)
        turtle.left(90)
        mink(n-1,x/4)
        turtle.left(90)
        mink(n-1,x/4)
        turtle.right(90)
        mink(n-1,x/4)

def koch(n,x):
    if n<=1:
        turtle.forward(x)
    else:
        koch(n-1,x/3)
        turtle.left(60)
        koch(n-1,x/3)
        turtle.right(120)
        koch(n-1,x/3)
        turtle.left(60)
        koch(n-1,x/3)

def flake(n,x):
    turtle.left(60)
    for _ in range(3):
        koch(n,x)
        turtle.right(120)

def setup():
    global turtle
    size(dim, dim)
    turtle = Turtle(10, height / 2 + 50)    
    
    background(255)
    
    # mink(4,400)
    flake(5,300)


def draw():
    pass  # Nothing to do in draw
