import json, sys
from network import internet_on
from firebase1 import Firebase
from logger import Logger

class Synchronising():
    p = None
    log = None
    gpsdata = None
    envdata = None
    config = None

    def run(self):
        with open('./config/config.json', 'r') as conf:
            self.config = json.load(conf)

        self.p = Firebase()    
        
    def post(self):
        if not len(self.gpsdata) < 1:
            for rows in self.gpsdata:
                #convert tuple(rows) to json
                jsondata = {"Data number": rows[0], "Device ID": rows[1], "Device Area": rows[2],
                            "Latitude": rows[4], "Longitude": rows[5], "Fix": rows[6],
                            "Quality": rows[7], "Date": rows[8], "Time": rows[9]}
                self.p.post_gps(jsondata)
                self.log.mark_upload(rows[0], self.config["DATA_FILES"]["GPS_DATA"])
        if not len(self.envdata) < 1:
            for rows in self.envdata:
                #convert tuple(rows) to json
                jsondata = {"Data number": rows[0], "Device ID": rows[1], "Device Area": rows[2],
                            "Temperature": rows[4], "Relative Humidity": rows[5], "Date": rows[6], "Time": rows[7]}
                self.p.post_sensor(jsondata)
                self.log.mark_upload(rows[0], self.config["DATA_FILES"]["ENVIRONMENT_DATA"])
        self.log.close()

    def networkCheck(self):
        return internet_on()

    def read(self):
        self.log = Logger()
        data = self.log.read()
        self.gpsdata = data[0]
        self.envdata = data[1]