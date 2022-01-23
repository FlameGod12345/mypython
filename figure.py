import turtle as a

def star(size, points):
    tipcorner = 5
    cavity = ( 360 + points * tipcorner ) / points 
    for x in range(points * 2):
        a.forward(size)
        if x % 2 == 0:
            a.left(320 - tipcorner)
        else:
            a.right(320 - cavity)
star(120, 6)
