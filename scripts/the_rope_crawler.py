#!/usr/bin/env python
import numpy as np

class Bot():
    """
    Class represents bot in global euclidean coordinates
    """
    def __init__(self, bot_width, bot_heigth, init_reel_radius, current_reel_radius):
        self.w = bot_width
        self.h = bot_heigth
        self.init_reel_radius = init_reel_radius
        # Assuming that bot is position perfectly in the middle
        self.setCurrentStatus(0, 0, current_reel_radius)
    
    def setCurrentStatus(self, x, y, current_reel_radius):
        self.x = x
        self.y = y
        self.current_reel_radius = current_reel_radius


class RopeCrawler():
    """
    Class that calculates required servos working time, 
    based on current position and desired position
    """
    def __init__(self, bot, box_width, box_height):
        self.bot = bot
        self.box_width = box_width
        self.box_height = box_height
    
    def getDirectionVector(self, x, y):
        current_length = self._calculateLength(self.bot.x, self.bot.y)
        desired_length = self._calculateLength(x, y)
        return desired_length - current_length

    def _calculateLength(self, x, y):
        width = self.box_width - self.bot.w
        heigth = self.box_height - self.bot.h

        l1 = (width + x) ** 2 + (heigth - y) ** 2
        l2 = (width - x) ** 2 + (heigth - y) ** 2
        l3 = (width - x) ** 2 + (heigth + y) ** 2
        l4 = (width + x) ** 2 + (heigth + y) ** 2
        
        return np.sqrt(np.array([l1, l2, l3, l4])) / 2

    def _calculateTurns(self, length_arr):
        circumference = 2 * np.pi * self.bot.current_reel_radius
        return length_arr / circumference

    def getSpinningVelocity(self, x_to, y_to):
        vector = self.getDirectionVector(x_to, y_to)
        turns = self._calculateTurns(vector)
        return turns / np.max(np.abs(turns))
