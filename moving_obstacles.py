import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.pyplot import figure
from shapely.geometry import Point, Polygon
import numpy as np

filename = "input2.txt"

def readFromFile(file_name):
    fin = open(file_name, "r")
    # Dòng 1: Kích thước [w,h] của bản đồ
    size = fin.readline().strip("\n").split(",")
    width = int(size[0])
    height = int(size[1])
    # Dòng 2: 2 cặp toạ độ (sX,sY),(gX,gY)
    point = fin.readline().strip("\n").split(",")
    start = (int(point[0]), int(point[1]))
    goal = (int(point[2]), int(point[3]))
    # Dòng 3: Số lượng chướng ngại vật (đa giác) n
    nObj = int(fin.readline())
    verticeslist = []
    # n dòng tiếp theo: Dòng thứ i: Chứa thông tin đa giác thứ i: Cứ 2 cặp số là tọa độ của một đỉnh.
    for i in range(nObj):
        tmp = fin.readline().strip("\n").split(",")
        for j in range(len(tmp)):
            tmp[j] = float(tmp[j])
        #tmp = list(map(float, tmp))
        verticeslist.append(tmp)
    fin.close()
    return width, height, start, goal, verticeslist

def makeObjects(verticeslist):
    objects = []
    for i in verticeslist:
        vertices = []
        for j in range(0, len(i) - 1, 2):
            vertices.append((i[j], i[j+1]))
        objects.append(Polygon(vertices))
    return objects
    
def moveObjects(verticeslist, dist):
    newverticeslist = []
    for i in range(len(verticeslist)):
        tmp = []
        for j in range(len(verticeslist[i])):
            tmp.append(verticeslist[i][j] + dist if j%2 == 0 else verticeslist[i][j])
        newverticeslist.append(tmp)
    
    return newverticeslist

w, h, s, g, vl = readFromFile(filename)
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def drawMap(w, h, s, g, vl):
    for i in range(0, 20):
        plt.clf()
        dist = 0
        if (i % 2 == 0):
            dist = 4
        #else:
        #    dist = -0.5
        plt.xlim(0, w)
        plt.ylim(0, h)
        plt.scatter(s[0],s[1], marker = "*", color = "green")
        plt.scatter(g[0],g[1], marker = "*", color = "red")
        coors = []
        movingvl = moveObjects(vl, dist)

        objs = makeObjects(movingvl)
        for k in range(len(objs)):
            x,y = objs[k].exterior.xy
            coors.append((x,y))
            plt.plot(coors[k][0], coors[k][1])

        plt.pause(0.5)    
    #plt.show()

def main():
    #filename = input()

#    w, h, s, g, vl = readFromFile(filename)
#    objs = makeObjects(vl)
    anim = FuncAnimation(fig, drawMap(w, h, s, g, vl), interval=20)
    plt.show()
#    drawMap(w,h,s,g,objs)

main()