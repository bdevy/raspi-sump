""" Module to send metrics to storage systems. """

# Raspi-sump, a sump pump monitoring system.
# Al Audet
# http://www.linuxnorth.org/raspi-sump/
#
# All configuration changes should be done in raspisump.conf
# MIT License -- http://www.linuxnorth.org/raspi-sump/license.html

import configparser
from raspisump import log
from influxdb import InfluxDBClient
from datetime import datetime

config = configparser.RawConfigParser()
config.read("/home/pi/raspi-sump/raspisump.conf")

configs = {
    "zabbix_host": config.get("storage", "zabbix_host"),
    "influxdb_host": config.get("storage", "influxdb_host"),
    "influxdb_port": config.get("storage", "influxdb_port"),
    "influxdb_username": config.get("storage", "influxdb_username"),
    "influxdb_password": config.get("storage", "influxdb_password"),
    "influxdb_database": config.get("storage", "influxdb_database"),
    "influxdb_measurement": config.get("storage", "influxdb_measurement"),
    "influxdb_location": config.get("storage", "influxdb_location")
}


def something(metrics):
    '''receives metrics from sensor collection function,
       determines and calls storage mechanisms.'''


def csv_wrter(value, csv_file):
    '''Store data using original csv method.'''
    log.log_reading(value, csv_file)


def zabbix_writer(metrics):
    '''Store data using zabbix trapper method.'''



def influxdb_writer(values):
    '''Store data using influxdb method.'''

    dbClient = InfluxDBClient(host=configs["influxdb_host"], port=configs["influxdb_port"], username=configs["influxdb_username"], password=configs["influxdb_password"], database=configs["influxdb_database"])

    jbody = []
    jbody.append(
        {
            "measurement": configs["influxdb_measurement"],
            "tags": {
                "Location": configs["influxdb_location"]
            },
            "fields": {
                "waterlevel": values["depth"],
                "watertemp": values["temp"]
            }
        }
    )

    dbResult = dbClient.write_points(jbody)
    #log errors to some log file
