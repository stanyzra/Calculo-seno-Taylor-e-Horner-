# -*- coding: utf-8 -*-
import math
    
def horner(x, facList):
    y = x**2
    result = facList[0]
    sizeList = len(facList)
    for i in range(sizeList):
        if i + 1 == sizeList:
            return result
        #print("{} + {} * {} = {}".format(result, x, facList[i], result + y * facList[i]))
        result = facList[i+1] + y * result

def sinCalc(x):
    facList = []
    for i in range(9):
        exp = (i*2)+1 # expoente para sen
        facList.append((-1)**(i)*1/math.factorial(exp))
    
    facList.reverse()
    hornerSin = horner(x, facList)*x
    return (hornerSin)
     
def cosCalc(x):
    facList = []
    for i in range(9):
        exp = (i*2) # expoente para cos
        facList.append((-1)**(i)*1/math.factorial(exp))
        
    facList.reverse()
    hornerCos = horner(x, facList)
    return (hornerCos)

def verification(x):
    if (x >= 2*math.pi):
        x = x-math.floor(x/(2*math.pi))*math.pi*2
    if (x <= math.pi/4):
        sin = str(sinCalc(x))[:12]
        cos = str(cosCalc(x))[:12]
        return print("sin: {} | cos: {}".format(sin, cos))
    elif (math.pi >= x and x > math.pi/4):
        sin = str(cosCalc(math.pi/2-x))[:12]
        cos = str(sinCalc(math.pi/2-x))[:12]
        return print("sin: {} | cos: {}".format(sin, cos))
    elif (3*math.pi/4 >= x and x > math.pi/2):
        sin = str(cosCalc(x-math.pi/2))[:12]
        cos = str(sinCalc(x-math.pi/2))[:12]
        return print("sin: {} | cos: {}".format(sin, cos))     
    elif (math.pi >= x and x > (3*math.pi)/4):
        sin = str(sinCalc(math.pi-x))[:12]
        cos = str(cosCalc(math.pi-x))[:12]
        return print("sin: {} | cos: {}".format(sin, cos))
    elif (x > math.pi):
        sin = str(-1*sinCalc(x-math.pi))[:12]
        cos = str(-cosCalc(x-math.pi))[:12]
        return print("sin: {} | cos: {}".format(sin, cos))
    
deg = input("Insira um valor (graus): ")
rad = float(deg)* (math.pi / 180)
print("graus: {} | radianos: {}".format(deg, rad))
(verification(rad))

