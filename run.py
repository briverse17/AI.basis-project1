# -*- coding: utf-8 -*-
# @Author: Doan Quang Tuan - Le Hoang Sang

#from AStar2 import AStar
from AStar import AStar
from ARAStar import ARAStar
from GUI import *

if __name__ == "__main__":
    if len(sys.argv) == 3 or len(sys.argv) == 5:
        if len(sys.argv) == 3:
            input_name, output_name = sys.argv[1], sys.argv[2]
            
            findPath = AStar(input_name)
            map, map_width, map_height, start, goal, objects = findPath.getMapInformation()
            #smap, map_width, map_height, start, goal = findPath.getMapInformation()


            screen_width = ITEM_WIDTH * map_width + MARGIN * map_width
            screen_height = ITEM_HEIGHT * map_height + MARGIN * map_height


            gui = GUI(map, map_width, map_height, start, goal, screen_width, screen_height, "A Star")
            gui.drawMap()
            gui.ready()

            findPath.runAStar(gui, input_name, output_name)

            gui.wait()

        else:
            input, output, epsilon, tmax = sys.argv[1], sys.argv[2], float(sys.argv[3]), int(sys.argv[4])
            findPath = ARAStar()
            findPath.runARAStar(input, output, epsilon, tmax)

    else:
        Notification().error("Error", "Parameter is incorrect\nExample>main.exe input.txt output.txt")
