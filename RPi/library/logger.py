import sqlite3, json, sys
from sqlite3 import Error
from filechecker import *

class Logger():
    def __init__(self):
        with open('./config/config.json', 'r') as conf:
            self.config = json.load(conf)
        try:
            if not containsdir('./data/'):
                makedir('./data/')
            self.conn = sqlite3.connect('./data/' + self.config["DATA_FILES"]["DATABASE"])
        except Error as e:
            print (e)
        
    def write(self, data):
        c = self.conn.cursor()
        print(data[0])
        c.execute(data[0])
        print(data[1])
        if data[1] != "":
            c.execute(data[1])
        self.conn.commit()

    def read(self):
        c = self.conn.cursor()    
        c.execute('select * from gps_data where data_uploaded=0')
        gpsdata = c.fetchall()
        c.execute('select * from sensor_data where data_uploaded=0')
        envdata = c.fetchall()
        return [gpsdata, envdata]

    def close(self):
        self.conn.close()

    def mark_upload(self, no, data):
        c = self.conn.cursor()
        if data == self.config["DATA_FILES"]["GPS_DATA"]:
            c.execute('update gps_data set data_uploaded=1 where id_no=?', (no,))
        elif data == self.config["DATA_FILES"]["ENVIRONMENT_DATA"]:
            c.execute('update environment_data set data_uploaded=1 where id_no=?', (no,))
        self.conn.commit()
