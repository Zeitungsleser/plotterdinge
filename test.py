import math, numpy
import subprocess

sizeSupIm = 700

f = open('cursed2.hpgl', 'w')
f.write("IN;PU;SP1;")

def writePoints(pointArr):
    s = "PU"+str(pointArr[0][0])+","+str(pointArr[0][1])+";PD"
    for point in pointArr:
        s = s + str(point[0]) + "," + str(point[1]) + ","
    s = s[:-1] + ";PU;"
    f.write(s)

def kurve(px,py, center):
    xt = lambda t: int(center[0]+sizeSupIm/2*math.cos(px*t))
    yt = lambda t: int(center[1]+sizeSupIm/2*math.sin(py*t))

    ts = numpy.linspace(0,2*math.pi, 100)
    arr = []
    for t in ts:
        arr.append([xt(t),yt(t)])
    writePoints(arr)

for x in range(14):
    for y in range(9):
        center = [sizeSupIm/2+100+(100+sizeSupIm)*(x), sizeSupIm/2+100+(100+sizeSupIm)*y]
        kurve(x+1,y+1,center)

f.write("PU;IN;")
