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
        return print("sin: {:.10f} | cos: {:.10f}".format(sinCalc(x), cosCalc(x)))
    elif (math.pi >= x and x > math.pi/4):
        return print("sin: {:.10f} | cos: {:.10f}".format(cosCalc(math.pi/2-x), sinCalc(math.pi/2-x)))
    elif (3*math.pi/4 >= x and x > math.pi/2):
        return print("sin: {:.10f} | cos: {:.10f}".format(cosCalc(x-math.pi/2), sinCalc(x-math.pi/2)))     
    elif (math.pi >= x and x > (3*math.pi)/4):
        return print("sin: {:.10f} | cos: {:.10f}".format(sinCalc(math.pi-x), cosCalc(math.pi-x)))
    elif (x > math.pi):
        return print("sin: {:.10f} | cos: {:.10f}".format(-1*sinCalc(x-math.pi), -cosCalc(x-math.pi)))
    
deg = input("Insira um valor (graus): ")
rad = float(deg)* (math.pi / 180)
print("graus: {} | radianos: {}".format(deg, rad))
(verification(rad))

