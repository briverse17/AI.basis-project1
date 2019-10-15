from AStar import AStar
from GUI import *

if __name__ == "__main__":
    #if len(sys.argv) == 3:
    input_name = "input1.txt"
    output_name = "output1.txt"
    findPath = AStar(input_name)
    map, map_width, map_height, start, goal = findPath.getMapInformation()
    screen_width = ITEM_WIDTH * map_width + MARGIN * map_width
    screen_height = ITEM_HEIGHT * map_height + MARGIN * map_height
    gui = GUI(map, map_height, map_width, start, goal,screen_width, screen_height, "A Star")
    gui.drawMap()
    gui.ready()
    findPath.runAStar(gui, input_name, output_name)
    gui.wait()
        