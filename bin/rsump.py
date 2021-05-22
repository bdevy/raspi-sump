#!/usr/bin/env python

# Raspi-sump, a sump pump monitoring system.
# Al Audet
# http://www.linuxnorth.org/raspi-sump/
#
# All configuration changes should be done in raspisump.conf
# MIT License -- http://www.linuxnorth.org/raspi-sump/license.html

import time

try:
    import ConfigParser as configparser # Python2
except ImportError:
    import configparser # Python3
from raspisump import reading

config = configparser.RawConfigParser()

config.read('/home/pi/raspi-sump/raspisump.conf')
reading_interval = config.getint('pit', 'reading_interval')
monitor_temp = config.getint('pit', 'monitor_temperature')

if reading_interval == 0:
    depth = reading.water_depth()
    values = {
        "depth": depth
    }
    if monitor_temp:
        values["temp"] = reading.temp_reading()

    store_values(values)
else:
    while True:
        depth = reading.water_depth()
        values = {
            "depth": depth
        }

        if monitor_temp:
            values["temp"] = reading.temp_reading()

        store_values(values)
        time.sleep(reading_interval)


def store_values(values):
    ''' Decide which storage mechanism to use. '''

    if use_csv:
        storage.csv_writer(values[depth], "waterlevel")

        if monitor_temp:
            storage.csv_writer(values[temp], "watertemp")

    if use_zabbix:
        #storage.zabbix_writer(values)
        pass

    if use_influxdb:
        storage.influxdb_writer(values)

