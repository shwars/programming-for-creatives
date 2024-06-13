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

def setup():
    size(400, 400)
    background(255)
    
    turtle = Turtle(width / 2, height / 2)
    
    # Draw a square
    for _ in range(4):
        turtle.forward(100)
        turtle.right(90)

def draw():
    pass  # Nothing to do in draw
