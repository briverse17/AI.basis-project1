import math
from PriorityQueue import PriorityQueue
from itertools import permutations
from File_NPoint import *
from GUI_NPoint import *
from Heuristic import *

# A* search algorithm
class AStarNPoint:
    def __init__(self, input_name = 'input1.txt'):
        self.minStep = -1
        self.minPath = []
        self.g_score = {}
        self.f_score = {}
        self.close_set = set()
        self.open_set = PriorityQueue()
        self.came_from = {}  # father
        self.map, self.map_width, self.map_height, self.start, self.pick_up, self.goal = readFromFile(input_name)

        self.pick_up_set = []

    def getMapInformation(self):
        return self.map, self.map_width, self.map_height, self.start, self.pick_up, self.goal

    def getStart(self):
        return self.start

    def trackingPath(self, start, goal):
        data = []
        current = tuple(goal)
        while current in self.came_from:
            data.append(current)
            current = self.came_from[current]
        data.append(start)
        data.reverse()
        self.minStep += len(data)
        return data

    def isValid(self, neighbor):
        map = self.map
        return (0 <= neighbor[0] < map.shape[0]) and (0 <= neighbor[1] < map.shape[1]) and (map[neighbor[0]][neighbor[1]] == 0)

    def aStar(self, curr, next, gui):
        self.g_score = {}
        self.f_score = {}
        self.close_set = set()
        self.open_set = PriorityQueue()
        self.came_from = {}  # father

        self.open_set.put(curr, 0)
        self.g_score[curr] = 0
        self.f_score[curr] = self.g_score[curr] + heuristic(curr, next)
       # neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
        neighbors = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        while not self.open_set.empty():
            _, current = self.open_set.get()
            if current == next:
                return self.trackingPath(curr, next)
            self.close_set.add(current)
            #gui.updateMap(current, CURRENT_COLOR)
            for direction in neighbors:
                neighbor = (current[0] + direction[0], current[1] + direction[1])
                if not self.isValid(neighbor):
                    continue
                if neighbor in self.close_set and self.g_score[current] + 1 >= self.g_score[neighbor]:
                    continue
                #gui.updateMap(neighbor, NEIGHBOR_COLOR)
                if neighbor not in self.g_score or self.g_score[current] + 1 < self.g_score[neighbor]:
                    self.came_from[neighbor] = current
                    self.g_score[neighbor] = self.g_score[current] + 1
                    self.f_score[neighbor] = self.g_score[neighbor] + heuristic(neighbor, next)
                    self.open_set.put(neighbor, self.f_score[neighbor])
        
        return []
    
    def aStarNPoint(self, gui):
        minStep = 0
        minPath = []

        permutation = self.pickupPermute()
        for i in range(len(permutation)):
            self.pick_up_set = list(permutation[i])
            curr = self.start
            next = self.pick_up_set.pop(0)
            
            self.minPath = self.minPath + self.aStar(curr, next, gui)

            while self.pick_up_set:
                curr = next
                next = self.pick_up_set.pop(0)
                self.minPath = self.minPath + self.aStar(curr, next, gui)
        
            curr = next
            next = self.goal
            self.minPath = self.minPath + self.aStar(curr, next, gui)

            if((i == 0) or (self.minStep < minStep)):
                minStep = self.minStep
                minPath = self.minPath
            
        self.minStep = minStep
        self.minPath = minPath
        return self.minPath



    def pickupPermute(self):
        pickupPermute = permutations(self.pick_up)
        return list(pickupPermute)

    def findNextPoint(self, current):
        dis = []
        for i in range(len(self.pick_up_set)):
            dis.append(heuristic(current, self.pick_up_set[i]))
        return dis.index(min(dis))

    def runAStarNPoint(self, gui, input_name = 'input1.txt'):
        global sum_delay
        sum_delay = 0
        START_TIME = time.clock()
        self.map, self.map_width, self.map_height, self.start, self.pick_up, self.goal = readFromFile(input_name)
        self.minPath = self.aStarNPoint(gui)
        
        if self.minStep == -1:
            Notification().alert("Notification", "Path not found!")
        else:
            gui.drawPath(self.minPath)
            Notification().alert("Time: ",
                                 repr(time.clock() - START_TIME - sum_delay) + "s\nStep: " + repr(self.minStep))