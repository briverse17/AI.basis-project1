import pygame
from tkinter import messagebox
from tkinter import Tk
import time
import sys

# color
NEIGHBOR_COLOR = (255, 255, 153) #yellow
WALL_COLOR = (0, 0, 0)
START_GOAL_COLOR = (255, 0, 0) #red
CURRENT_COLOR = (102, 102, 255) #blue
BACKGROUND_COLOR = (204, 255, 229)
PICK_UP_COLOR = (0,255,43) #green
PART_MIN_COLOR = (255,102,0) #organce

# variable
MARGIN = 1
ITEM_WIDTH = 15
ITEM_HEIGHT = 15

# time
DELAY_TIME = 0.005  # 0.1s
sum_delay = 0

class GUI_NPoint():
    def __init__(self, map, map_width, map_height, start, pick_up, goal, screen_width, screen_height, screen_caption):
        self.map = map
        self.map_width = map_width
        self.map_height = map_height
        self.start = start
        self.pick_up = pick_up
        self.goal = goal
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen_caption = screen_caption
        pygame.init()
        pygame.display.set_caption(self.screen_caption)
        self.screen = pygame.display.set_mode([screen_width, screen_height])

    def drawMap(self):
        width = self.map_width
        height = self.map_height
        matrix = self.map
        root = self.start
        pick_up = self.pick_up
        des = self.goal
        self.screen.fill(BACKGROUND_COLOR)
        x = 0
        while x < width:
            y = 0
            while y < height:
                if (matrix[x][y] == 1):
                    pygame.draw.rect(self.screen, WALL_COLOR,
                                     [(ITEM_WIDTH + MARGIN) * y + MARGIN, (ITEM_HEIGHT + MARGIN) * x + MARGIN,
                                      ITEM_WIDTH,
                                      ITEM_HEIGHT])
                y = y + 1
            x = x + 1
        pygame.draw.rect(self.screen, START_GOAL_COLOR,
                         [(ITEM_WIDTH + MARGIN) * root[1] + MARGIN, (ITEM_HEIGHT + MARGIN) * root[0] + MARGIN,
                          ITEM_WIDTH,
                          ITEM_HEIGHT])
        pygame.draw.rect(self.screen, START_GOAL_COLOR,
                         [(ITEM_WIDTH + MARGIN) * des[1] + MARGIN, (ITEM_HEIGHT + MARGIN) * des[0] + MARGIN, ITEM_WIDTH,
                          ITEM_HEIGHT])
        for i in range(len(pick_up)):
            pygame.draw.rect(self.screen, PICK_UP_COLOR,
                         [(ITEM_WIDTH + MARGIN) * pick_up[i][1] + MARGIN, (ITEM_HEIGHT + MARGIN) * pick_up[i][0] + MARGIN, ITEM_WIDTH,
                          ITEM_HEIGHT])
        pygame.display.flip()

    def updateMap(self, pos, color):
        global sum_delay
        if self.start != pos:
            pygame.draw.rect(self.screen, color,
                             [(ITEM_WIDTH + MARGIN) * pos[1] + MARGIN, (ITEM_HEIGHT + MARGIN) * pos[0] + MARGIN,
                              ITEM_WIDTH,
                              ITEM_HEIGHT])
            pygame.display.update()
        time.sleep(DELAY_TIME)
        sum_delay = sum_delay + DELAY_TIME

    def drawPath(self, path):
        pick_up = self.pick_up
        des = self.goal
        for pos in path:
            self.updateMap(pos, PART_MIN_COLOR)
        pygame.draw.rect(self.screen, START_GOAL_COLOR,
                         [(ITEM_WIDTH + MARGIN) * des[1] + MARGIN, (ITEM_HEIGHT + MARGIN) * des[0] + MARGIN, ITEM_WIDTH,
                          ITEM_HEIGHT])
        for i in range(len(pick_up)):
            pygame.draw.rect(self.screen, PICK_UP_COLOR,
                         [(ITEM_WIDTH + MARGIN) * pick_up[i][1] + MARGIN, (ITEM_HEIGHT + MARGIN) * pick_up[i][0] + MARGIN, ITEM_WIDTH,
                          ITEM_HEIGHT])
        pygame.display.update()

    def ready(self):
        Notification().alert(self.screen_caption, "Press OK to start")

    def wait(self):
        while True:
            event = pygame.event.poll()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


class Notification():
    def alert(self, title, content):
        Tk().wm_withdraw()
        messagebox.showinfo(title, content)

    def error(self, title, content):
        Tk().wm_withdraw()
        messagebox.showerror(title, content)
