import json, sys, serial
from logger import Logger
from module import Module
import RPi.GPIO as GPIO

class Monitoring():
    gpsdata = None
    sensordata = None
    config = None

    def run(self):
        with open('./config/config.json', 'r') as conf:
            self.config = json.load(conf)
        self.gpscheck = True
        self.sensorcheck = True

    '''
    Serial ser - the Serial port
    GPIO gpio - the GPIO
    ''' 
    def read(self, ser, gpio):
        mod = Module()
        mod.readsensor(gpio)
        mod.readgps(ser)
        self.sensordata = mod.sensordata
        self.gpsdata = mod.gpsdata


    def store(self):
        log = Logger()
        log.write(self.gpsdata)
        log.write(self.sensordata[0])
        #log.write(self.sensordata[1])
