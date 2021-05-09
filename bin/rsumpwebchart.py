#!/usr/bin/env python

# Raspi-sump, a sump pump monitoring system.
# Al Audet
# http://www.linuxnorth.org/raspi-sump/
#
# All configuration changes should be done in raspisump.conf
# MIT License -- http://www.linuxnorth.org/raspi-sump/license.html

import time
from raspisump import webchart
import configparser

config = configparser.RawConfigParser()

config.read('/home/pi/raspi-sump/raspisump.conf')
monitor_temp = config.getint('pit', 'monitor_temperature')

def main():
    '''Pass variables to webchart.py'''
    year = time.strftime('%Y')
    month = time.strftime('%m')
    today = time.strftime('%Y%m%d')
    homedir = '/home/pi/raspi-sump/'
    webchart.create_folders(year, month, homedir)
 
    webchart.create_chart(homedir, 'waterlevel')
    webchart.copy_chart(year, month, today, homedir, 'waterlevel')

    if monitor_temp:
        webchart.create_chart(homedir, 'watertemp')
        webchart.copy_chart(year, month, today, homedir, 'watertemp')


if __name__ == '__main__':
    main()
