#!/usr/bin/env python
from the_rope_crawler import *
import math

if __name__=='__main__':
    bot_w = bot_h = 20
    reel_d = 2

    box_w = box_h = 400

    bot = Bot(bot_w, bot_h, reel_d, reel_d)
    crawler = RopeCrawler(bot, box_w, box_h)
    
    bot_to_box_edge = (box_h - bot_h) / 2
    length_in_origin = crawler._calculateLength(0, 0)
    test = length_in_origin == np.array([np.sqrt(2 * bot_to_box_edge ** 2)] * 4)
    result = 'PASS' if test.all() else 'FAIL'
    print('[{}] Rope length calculation in origin test'.format(result))

    condition = length_in_origin < crawler._calculateLength(5, 0)
    test = condition == [1, 0, 0, 1]
    result = 'PASS' if test.all() else 'FAIL'
    print('[{}] Moving along X-axis in positive direction test'.format(result))

    condition = length_in_origin > crawler._calculateLength(-5, 0)
    test = condition == [1, 0, 0, 1]
    result = 'PASS' if test.all() else 'FAIL'
    print('[{}] Moving along X-axis in negative direction test'.format(result))

    condition = length_in_origin < crawler._calculateLength(0, 5)
    test = condition == [0, 0, 1, 1]
    result = 'PASS' if test.all() else 'FAIL'
    print('[{}] Moving along Y-axis in positive direction test'.format(result))

    condition = length_in_origin > crawler._calculateLength(0, -5)
    test = condition == [0, 0, 1, 1]
    result = 'PASS' if test.all() else 'FAIL'
    print('[{}] Moving along Y-axis in negative direction test'.format(result))

    condition = length_in_origin > crawler._calculateLength(5, 5)
    test = condition == [0, 1, 0, 0]
    result = 'PASS' if test.all() else 'FAIL'
    print('[{}] Moving along Y-axis in negative direction test'.format(result))

    print(crawler.getServoTime(5, 0, 1))