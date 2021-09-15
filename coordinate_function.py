def slope(x1,y1,x2,y2):
    m = (y2-y1)/(x2-x1)
    b= y1 - (m*x1)   
#    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return m, b

def plane(m, x, b):
    y = m*x + b
    return y