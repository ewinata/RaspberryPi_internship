import time, json, sys, serial
from monitoring import Monitoring
from synchronising import Synchronising
import RPi.GPIO as GPIO

class Engine():

    ser = None

    def __init__(self, arg):
        print("Running main engine...")
        with open('./config/config.json', 'r') as conf:
                config = json.load(conf)
        if arg == '1':
            print("Reading...")
            try:
                self.ser = serial.Serial()
                self.ser.port = config["SERIAL_PORTS"]["GPS_SERIAL_PATH"]
                self.ser.baudrate = 9600
                self.ser.timeout = 0.5
                if not self.ser.is_open:
                    self.ser.open()
                GPIO.setwarnings(False)
                GPIO.setmode(GPIO.BCM)
                self.readdata(GPIO)
                GPIO.cleanup()
            finally:
                pass
        elif arg == '2':
            self.pushdata()

    def readdata(self, gpio):
        m = Monitoring()
        m.run()
        m.read(self.ser, gpio)
        m.store()

    def pushdata(self):
        s = Synchronising()
        if s.networkCheck():
            s.run()
            s.read()
            s.post()
