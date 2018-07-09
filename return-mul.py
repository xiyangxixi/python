import  math
def move(x, y, step, angle=0):
    rx = x + step * math.cos(angle)
    ry = y - step * math.sin(angle)
    return  rx, ry
print(move(100, 100, 60, math.pi / 6))