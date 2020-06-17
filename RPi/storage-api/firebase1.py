import json
from firebase import firebase

class Firebase():
    def __init__(self):
        with open('./config/config.json', 'r') as conf:
            self.config = json.load(conf)
        self.fb = firebase.FirebaseApplication(self.config['STORAGE']['FIREBASE_URL'], None)

    def post_gps(self, data):
        """Posts gps data to firebase
        json data - the data to be posted
        """
        self.fb.post(self.config['STORAGE']['FIREBASE_GPS_COLLECTION'] ,data)
        
    def post_sensor(self, data):
        """Posts sensor data to firebase
        json data - the data to be posted
        """
        self.fb.post(self.config['STORAGE']['FIREBASE_SENSOR_COLLECTION'], data)
