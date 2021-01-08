from turtle import Turtle as t

class Cartesian(t):
    
    def __init__(self):
        super().__init__()
        self.speed(0.1)
        self.hideturtle()
    
    def creation_axe_x(self, star, stop, step):
        """Creation of the axe X

        Args:
            star (float): this is the position where you want to go your "one", normally have to be equal to |step|
            stop (float): this have to be the half of the width of the screen
            step (float): this is the distance between every value of the axe
        """        
        for i in range(star, stop, step):
            self.goto(i,0)
            self.goto(i, 1)
            self.goto(i, -1)
            self.goto(i, 0)
            self.write(arg = int(i/20), align = "center", font = ("Arial", 9, "normal"))
        self.goto(0,0)
       
            
    def creation_axe_y(self, star, stop, step):
        """Creation of the axe Y

        Args:
            star (float): this is the position where you want to go your "one", normally have to be equal to |step|
            stop (float): this have to be the half of the width of the screen
            step (float): this is the distance between every value of the axe
        """       
        for i in range(star, stop, step):
            self.goto(0, i)
            self.goto(1, i)
            self.up()
            self.goto(4,i)
            self.down()
            self.write(arg = int(i/20), align = "left", font = ("Arial", 10, "normal"))
            self.goto(-1, i)
            self.goto(0, i)
        self.goto(0,0)
            