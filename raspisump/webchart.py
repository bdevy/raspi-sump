'''Create charts for viewing on Raspberry Pi Web Server.'''

# Raspi-sump, a sump pump monitoring system.
# Al Audet
# http://www.linuxnorth.org/raspi-sump/
#
# All configuration changes should be done in raspisump.conf
# MIT License -- http://www.linuxnorth.org/raspi-sump/license.htmlimport os

import os
import subprocess
import time
from raspisump import todaychart


def create_folders(year, month, homedir):
    '''Check if folders exist in charts folder and create them if they don't'''
    if not os.path.isdir('{}charts/{}/'.format(homedir, year)):
        _year = 'mkdir {}charts/{}'.format(homedir, year)
        create_year = _year.split(' ')
        subprocess.call(create_year)

    if not os.path.isdir('{}charts/{}/{}/'.format(homedir, year, month)):
        _month = 'mkdir {}charts/{}/{}'.format(homedir, year, month)
        create_month = _month.split(' ')
        subprocess.call(create_month)


def create_chart(homedir, csv_name):
    '''Create a chart of sump pit activity and save to web folder'''
    if csv_name == 'waterlevel':
        title = 'Water'
    elif csv_name == 'watertemp':
        title = 'Temperature'
    else:
        pass
    csv_file = '{}csv/{}-{}.csv'.format(
        homedir, csv_name, time.strftime('%Y%m%d')
        )
    filename = '{}charts/today_{}.png'.format(homedir, csv_name)
    bytes2str = todaychart.bytesdate2str('%H:%M:%S')
    todaychart.graph(csv_file, filename, bytes2str, title)


def copy_chart(year, month, today, homedir, csv_name):
    '''Copy today.png to year/month/day folder for web viewing'''
    copy_cmd = 'cp {}charts/today_{}.png {}charts/{}/{}/{}_{}.png'.format(
        homedir, csv_name, homedir, year, month, today, csv_name
        )
    copy_file = copy_cmd.split(' ')
    subprocess.call(copy_file)
