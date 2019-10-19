import math
#from PriorityQueue import PriorityQueue
from queue import SimpleQueue
from File import *
from GUI import *
from Heuristic import *


# A* search algorithm
class BFS:

    def __init__(self, input_name = 'input1.txt'):
        self.minStep = -1
        self.minPath = []
        self.close_set = set()
        #self.open_set = PriorityQueue()
        self.open_set = SimpleQueue()
        self.came_from = {}  # father
        self.map, self.map_width, self.map_height, self.start, self.goal = readFromFile(input_name)

    def getMapInformation(self):
        return self.map, self.map_width, self.map_height, self.start, self.goal

    def getStart(self):
        return self.start

    def trackingPath(self):
        data = []
        current = tuple(self.goal)
        while current in self.came_from:
            data.append(current)
            current = self.came_from[current]
        data.append(self.start)
        data.reverse()
        self.minStep = len(data)
        return data

    def isValid(self, neighbor):
        map = self.map
        return (0 <= neighbor[0] < map.shape[0]) and (0 <= neighbor[1] < map.shape[1]) and (map[neighbor[0]][neighbor[1]] == 0)

    def BFS(self, gui):
        self.open_set.put(self.start)
       # neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
        neighbors = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        while not self.open_set.empty():
            current = self.open_set.get()
            if current == self.goal:
                return self.trackingPath()
            self.close_set.add(current)
            gui.updateMap(current, CURRENT_COLOR)
            for direction in neighbors:
                neighbor = (current[0] + direction[0], current[1] + direction[1])
                if not self.isValid(neighbor):
                    continue
                if neighbor in self.close_set:
                    continue
                gui.updateMap(neighbor, NEIGHBOR_COLOR)
                if neighbor not in self.came_from:
                    self.open_set.put(neighbor)
                    self.came_from[neighbor] = current
                    #self.close_set.add(neighbor)
                
        return []

    def runBFS(self, gui, input_name = 'input1.txt'):
        global sum_delay
        sum_delay = 0

        START_TIME = time.clock()
        self.map, self.map_width, self.map_height, self.start, self.goal = readFromFile(input_name)
        self.minPath = self.BFS(gui)
 
        if self.minStep == -1:
            Notification().alert("Notification", "Path not found!")
        else:
            gui.drawPath(self.minPath)
            Notification().alert("Time: ",
                                 repr(time.clock() - START_TIME - sum_delay) + "s\nStep: " + repr(self.minStep))

