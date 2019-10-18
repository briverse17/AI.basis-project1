from AStar import AStar
from AStar_NPoint import AStarNPoint
from DFS import DFS
from GUI import *
from GUI_NPoint import *

if __name__ == "__main__":
        input_name = 'input2.txt'

        findPath = AStarNPoint(input_name)
        map, map_width, map_height, start, pick_up, goal = findPath.getMapInformation()
        print(start, pick_up, goal)
        screen_width = ITEM_WIDTH * map_width + MARGIN * map_width
        screen_height = ITEM_HEIGHT * map_height + MARGIN * map_height

        gui_n = GUI_NPoint(map, map_height, map_width, start, pick_up, goal, screen_width, screen_height, "A Star With N Pickup Point")
        gui_n.drawMap()
        gui_n.ready()

        findPath.runAStarNPoint(gui_n, input_name)

        gui_n.wait()
        #========================================
        # input_name = 'input1.txt'

        # findPath = AStar(input_name)
        # map, map_width, map_height, start, goal = findPath.getMapInformation()

        # screen_width = ITEM_WIDTH * map_width + MARGIN * map_width
        # screen_height = ITEM_HEIGHT * map_height + MARGIN * map_height

        # gui = GUI(map, map_height, map_width, start, goal, screen_width, screen_height, "A Star")
        # gui.drawMap()
        # gui.ready()

        # findPath.runAStar(gui, input_name)

        # gui.wait()
#     if sys.argv[1] == "AStar":
#             input_name = sys.argv[2]

#             findPath = AStar(input_name)
#             map, map_width, map_height, start, goal = findPath.getMapInformation()

#             screen_width = ITEM_WIDTH * map_width + MARGIN * map_width
#             screen_height = ITEM_HEIGHT * map_height + MARGIN * map_height

#             gui = GUI(map, map_height, map_width, start, goal, screen_width, screen_height, "A Star")
#             gui.drawMap()
#             gui.ready()

#             findPath.runAStar(gui, input_name)

#             gui.wait()

#     elif sys.argv[1] == "AStarNPoint":
#             input_name = sys.argv[2]

#             findPath = AStarNPoint(input_name)
#             map, map_width, map_height, start, pick_up, goal = findPath.getMapInformation()
            
#             screen_width = ITEM_WIDTH * map_width + MARGIN * map_width
#             screen_height = ITEM_HEIGHT * map_height + MARGIN * map_height

#             gui_n = GUI_NPoint(map, map_height, map_width, start, pick_up, goal, screen_width, screen_height, "A Star With N Pickup Point")
#             gui_n.drawMap()
#             gui_n.ready()

#             findPath.runAStarNPoint(gui_n, input_name)

#             gui_n.wait()

#     elif sys.argv[1] == "DFS":
#             input_name = sys.argv[2]

#             findPath = DFS(input_name)
#             map, map_width, map_height, start, goal = findPath.getMapInformation()
#             screen_width = ITEM_WIDTH * map_width + MARGIN * map_width
#             screen_height = ITEM_HEIGHT * map_height + MARGIN * map_height

#             gui = GUI(map, map_height, map_width, start, goal, screen_width, screen_height, "DFS")
#             gui.drawMap()
#             gui.ready()

#             findPath.runDFS(gui, input_name)

#             gui.wait()

#     elif sys.argv[1] == "USC":
#             input_name = sys.argv[2]

#             findPath = AStar(input_name)
#             map, map_width, map_height, start, goal = findPath.getMapInformation()

#             screen_width = ITEM_WIDTH * map_width + MARGIN * map_width
#             screen_height = ITEM_HEIGHT * map_height + MARGIN * map_height

#             gui = GUI(map, map_height, map_width, start, goal, screen_width, screen_height, "A Star")
#             gui.drawMap()
#             gui.ready()

#             findPath.runAStar(gui, input_name)

#             gui.wait()

#     elif sys.argv[1] == "USC":
#             input_name = sys.argv[2]

#             findPath = AStar(input_name)
#             map, map_width, map_height, start, goal = findPath.getMapInformation()

#             screen_width = ITEM_WIDTH * map_width + MARGIN * map_width
#             screen_height = ITEM_HEIGHT * map_height + MARGIN * map_height

#             gui = GUI(map, map_height, map_width, start, goal, screen_width, screen_height, "A Star")
#             gui.drawMap()
#             gui.ready()

#             findPath.runAStar(gui, input_name)

#             gui.wait()

#     else:
#         Notification().error("Error", "Parameter is incorrect")
