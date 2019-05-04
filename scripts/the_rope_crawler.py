#!/usr/bin/env python
import numpy as np

class Bot():
    """
    Class represents bot in global euclidean coordinates
    """
    def __init__(self, bot_width, bot_heigth):
        # Assuming that bot is position perfectly in the middle
        self.setCurrentPosition(0, 0)
        self.w = bot_width
        self.h = bot_heigth
    
    def setCurrentPosition(self, x, y):
        self.x = x
        self.y = y


class RopeCrawler():
    """
    Class that calculates required servos working time, 
    based on current position and desired position
    """
    def __init__(self, bot, box_width, box_height):
        self.bot = bot
        self.box_width = box_width
        self.box_height = box_height
    
    def moveTo(self, x, y):
        current_length = self.calculateLength(self.bot.x, self.bot.y)
        desired_length = self.calculateLength(x, y)
        return desired_length - current_length

    def calculateLength(self, x, y):
        width = self.box_width - self.bot.w
        heigth = self.box_height - self.bot.h

        l1 = (width + x) ** 2 + (heigth - y) ** 2
        l2 = (width - x) ** 2 + (heigth - y) ** 2
        l3 = (width - x) ** 2 + (heigth + y) ** 2
        l4 = (width + x) ** 2 + (heigth + y) ** 2
        
        return np.sqrt(np.array(l1, l2, l3, l4)) / 2