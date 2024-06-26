from queue import LifoQueue
from File import *
from GUI import *
from shapely.geometry import Point, Polygon
from shapely.geometry.polygon import LinearRing

# DFS search algorithm
class DFS:
    '''Depth-First Search algorithm'''
    def __init__(self, input_name = 'input1.txt'):
        '''Initialize the DFS class'''
        self.minStep = -1
        self.minPath = []
        self.close_set = set()
        self.open_set = LifoQueue()
        self.came_from = {}  # father
        self.map, self.map_width, self.map_height, self.start, self.goal, self.objects = readFromFile(input_name)

    def getMapInformation(self):
        return self.map, self.map_width, self.map_height, self.start, self.goal, self.objects

    def getStart(self):
        return self.start

    def trackingPath(self):
        '''Return the path from start to goal'''
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
        '''Check if a neighbor is a valid direction to go'''
        map = self.map
        objects = self.objects
        check = True
        #check neighbor[0] and neighbor[1] is in one of the objects or not
        for i in range(len(objects)):
            linearring = LinearRing(list(objects[i].exterior.coords))

            if (objects[i].contains(Point(neighbor[1], self.map_height -  neighbor[0] - 1)) or
                objects[i].touches(Point(neighbor[1], self.map_height - neighbor[0] - 1)) or
                linearring.contains(Point(neighbor[1], self.map_height - neighbor[0] - 1))):
                check = False
                break
        return (check and 0 <= neighbor[0] < map.shape[0]) and (0 <= neighbor[1] < map.shape[1]) and (map[neighbor[0]][neighbor[1]] == 0)
    
    def DFS(self, gui):
        '''The BFS function'''
        self.open_set.put(self.start)
        #neighbors is a list of tuples of directions
        neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
        #neighbors = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        #self.open_set is a LIFO queue
        while not self.open_set.empty():
            current = self.open_set.get()
            if current == self.goal:
                #the function gets here when it runned successfully (goal reached)
                #calls self.trackingPath to get the result
                return self.trackingPath()
            #not goal reached
            self.close_set.add(current)
            gui.updateMap(current, CURRENT_COLOR)
            for direction in neighbors:
                #for each current node, check all 8 of its neighbor
                neighbor = (current[0] + direction[0], current[1] + direction[1])
                if not self.isValid(neighbor):
                    continue
                if neighbor in self.close_set:
                    continue
                gui.updateMap(neighbor, NEIGHBOR_COLOR)
                if neighbor not in self.came_from:
                    self.open_set.put(neighbor)
                    self.came_from[neighbor] = current
        return []
        #the function gets here after iterating all nodes but couldn't reach self.goal

    def runDFS(self, gui, input_name = 'input1.txt'):
        '''Run the BFS function and print the result'''
        global sum_delay
        sum_delay = 0

        START_TIME = time.clock()
        self.map, self.map_width, self.map_height, self.start, self.goal, self.objects = readFromFile(input_name)
        self.minPath = self.DFS(gui)
 
        if self.minStep == -1:
            Notification().alert("Notification", "Path not found!")
        else:
            gui.drawPath(self.minPath)
            Notification().alert("Time: ",
                                 repr(time.clock() - START_TIME - sum_delay) + "s\nStep: " + repr(self.minStep))

