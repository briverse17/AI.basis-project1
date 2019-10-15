import numpy as np
from bresenham import bresenham


def readFromFile(file_name):
    fin = open(file_name, "r")
    # Dòng 1: Kích thước [w,h] của bản đồ
    size = fin.readline().strip("\n").split(",")
    width = int(size[0])
    height = int(size[1])

    # Dòng 2: 2 cặp toạ độ (sX,sY),(gX,gY)
    point = fin.readline().strip("\n").split(",")
    start = (height - int(point[1]), int(point[0]))
    goal = (height - int(point[3]), int(point[2]))
    # Dòng 3: Số lượng chướng ngại vật (đa giác) n
    nObj = int(fin.readline())

    # n dòng tiếp theo: Dòng thứ i: Chứa thông tin đa giác thứ i: Cứ 2 cặp số là tọa độ của một đỉnh.
    map = np.zeros((height, width))  # ma trận bản đồ

    for i in range(nObj):
        tmp = fin.readline().strip("\n").split(",")
        j = 0

        while(j != len(tmp)):
            if(j + 2 < len(tmp)):
                line = list(bresenham(int(tmp[j]), int(tmp[j + 1]), int(tmp[j + 2]), int(tmp[j + 3])))
            else:
                line = list(bresenham(int(tmp[j]), int(tmp[j + 1]), int(tmp[0]), int(tmp[1])))

            k = 0
            while(k != len(line)):
                map[height - line[k][1] - 1][line[k][0]] = 1
                k += 1

            j += 2
    fin.close()
    return map, width, height, start, goal


# def writeToFile(file_name, map, map_width, map_height, start, goal, step, path):
#     fout = open(file_name, "w")
#     fout.write("%s\n" % str(step))
#     if step != -1:
#         for coor in path:
#             fout.write(str(coor) + ' ')
#         fout.write("\n")
#         mapFile = map
#         for i in range(map_height):
#             for j in range(map_width):
#                 if map[i][j] == 1:
#                     mapFile[i][j] = 'o'
#                 elif map[i][j] == 0:
#                     mapFile[i][j] = '-'
#         for i, j in path:
#             mapFile[i][j] = 'x'
#         mapFile[start[0]][start[1]] = 'S'
#         mapFile[goal[0]][goal[1]] = 'G'
#         for row in mapFile:
#             for i in row:
#                 fout.write("%s " % i)
#             fout.write("\n")
    
#     fout.close()
