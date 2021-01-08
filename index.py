import turtle as t
from cartesianPlan import Cartesian
#*-------------------------------------------------Configuration-------------------------------------------------
widthScreen = 620
heightScreen = 620
screen = t.Screen()
screen.setup(widthScreen, heightScreen)
screen.tracer(0)

#*-------------------------------------------------Cartesian Plan-------------------------------------------------

cartesianPlan = Cartesian()

positions = [(20, 310, 20), (-20,-310 , -20)]

for position in positions:
    cartesianPlan.creation_axe_x(position[0], position[1], position[2])

for position in positions:
    cartesianPlan.creation_axe_y(position[0], position[1], position[2])

#*-------------------------------------------------Graficate Draw-------------------------------------------------
pencil = t.Turtle()
pencil.speed(0.1)

pencil.up()

def range_with_float(start, stop, step):
    """Range with float

    Args:
        start (int-float): the first value
        stop (int-float): the last value
        step (float-int): cantity that increments the start with every bucle

    Yields:
        [float]: []
    """    
    
    i = start
    while i < stop:
        yield i
        i += step

widthSecondCuadrant = widthScreen/2*-1
widthFirstCuadrant = widthScreen/2
valueStep = 0.1

for variable in range_with_float(widthSecondCuadrant, widthFirstCuadrant, valueStep):
    """Grafic of the function

    Args:
        widthSecondCuadrant (int): Limits of the grafic
        widthFirstCuadrant (int): Limits of the grafic        
        
        function (float): This let me choose the form of the function, in this case is a cuadratic function
    """    
    if variable == -600:
        function = variable ** 2
        pencil.up()
    pencil.goto((variable)*20, (variable**2)*20)
    pencil.down()
        

screen.update()

    


screen.mainloop()