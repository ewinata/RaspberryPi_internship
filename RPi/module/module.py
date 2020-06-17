import sys, serial
import RPi.GPIO as GPIO
from gps import GPS
from rh_temp_sensor import rh_temp_sensor

class Module():
    sensordata = None
    gpsdata = None
    
    def readsensor(self, gpio):

        print('Reading sensors...')
        #Rh_temp_sensor
        rhtdata = rh_temp_sensor()
        rhtdata.read(gpio)
        rhtarr = rhtdata.sqlquery()

        #Smoke_sensor
        #smodata = smoke_sensor()
        #smodata.read()

        #disdata
        
        #if data is valid... then
        self.sensordata = [rhtarr]

    def readgps(self, ser):
        data = GPS(ser)
        data.read()
        self.gpsdata = data.sqlquery()
