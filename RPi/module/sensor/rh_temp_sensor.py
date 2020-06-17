import RPi.GPIO as GPIO
import dht11, time, json
from datetime import datetime

class rh_temp_sensor():

    def __init__(self, temp=-1, rh=-1):
        with open('./config/config.json', 'r') as conf:
            self.config = json.load(conf)
        self.pin = self.config["GPIO"]["RH_TEMP_PIN"]
        self.temp = temp
        self.rh = rh


    def getarray(self):
        return [self.temp, self.rh]

        
    def read(self, gpio):
        instance = dht11.DHT11(self.pin)
        result = instance.read()
        if result.is_valid():
            self.temp = result.temperature
            self.rh = result.humidity

        #print(self.temp)
        #print(self.rh)


    def sqlquery(self):
        table = '''CREATE TABLE IF NOT EXISTS environment_sensor(
                id_no integer primary key,
                device_id integer,
                device_area text,
                data_uploaded int,
                temperature int,
                relative_humidity int
                dates text,
                time text);'''
        if self.temp > 0 and self.rh > 0:
            dt = datetime.now()
            id = self.config["DEVICE_ID"]["ID"]
            area = self.config["DEVICE_ID"]["AREA"]
            uploaded = 0
            date = str(dt.day) + '/' + str(dt.month) + '/' + str(dt.year)
            time = str(dt.hour) + '-' + str(dt.minute) + '-' + str(dt.second)
            query = '''insert into environment_sensor (device_id, device_area, data_uploaded, temperature, relative_humidity, dates, time)
                    values ({},{},{},{},{},{},{})'''.format(id, area, uploaded, self.temp, self.rh, date, time)
            return [table, query]
        return [table, ""]
