#!/usr/bin/python

import RPi.GPIO as GPIO

GPIO_PIN_NUMBER=14
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PIN_NUMBER, GPIO.IN, pull_up_down=GPIO.PUD_UP)
