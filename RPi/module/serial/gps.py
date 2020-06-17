import serial, json
from gps_decoder import *

class GPS:

    def __init__(self, ser, lat="", long="", fix="", quality="", valid=True):
        with open('./config/config.json', 'r') as conf:
            self.config = json.load(conf)
        self.id_no = self.config["DEVICE_ID"]["ID"]
        self.lat = lat
        self.long = long
        self.fix = fix
        self.quality = quality
        self.valid = valid
        self.ser = ser

    
    def read(self):
        count = 0

        while count < 2:
            dataCheck = False
            serial_read = self.ser.readline()
            try:
                result = None
                data = serial_read.decode("utf-8")
                if data.startswith('$'):
                    skip = False
                if data.startswith('$GPGGA'):
                    result = gpgga_convert(data)
                    if result is not None:
                        self.lat = result[0]
                        self.long = result[1]
                        self.quality = result[2]
                    count+=1
                elif data.startswith('$GPGSA'):
                    result = gpgsa_convert(data)
                    if result is not None:
                        self.fix = result[0]
                    count+=1
                if result is None:
                    self.valid = False
            except UnicodeDecodeError:
                #data is invalid
                self.valid = False
                return


    def check(self):
        return self.valid
        

    def serial_killer(self):
        self.ser.close()


    def sqlquery(self):
        table = '''CREATE TABLE IF NOT EXISTS gps_data(
                id_no integer primary key,
                device_id integer,
                device_area text,
                data_uploaded int,
                latitude real,
                longitude real,
                fix text,
                quality text,
                dates text,
                time text);'''
        if self.valid:
            dt = datetime.now()
            id = self.config["DEVICE_ID"]["ID"]
            area = self.config["DEVICE_ID"]["AREA"]
            uploaded = 0
            date = str(dt.day) + '/' + str(dt.month) + '/' + str(dt.year)
            time = str(dt.hour) + '-' + str(dt.minute) + '-' + str(dt.second)
            query = '''insert into gps_data (device_id, device_area, data_uploaded, latitude, longitude, fix, quality, dates, time)
                    values ({},{},{},{},{},{},{},{},{})'''.format(id, area, uploaded, self.lat, self.long, self.fix, self.quality, date, str(time))
            return [table, query]
        return [table, ""]
