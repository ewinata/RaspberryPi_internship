import Rpi.GPIO as GPIO
import time

#Constants
trigger_pin = 7
echo_pin = 11
static_time = 0.00001 #time required for HC-SR04 sensor to trigger
sound_speed = 34300 #cm per second

#Time Variables
start_time = 0.0
end_time = 0.0

def init() {
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(trigger_pin, GPIO.OUT, initial=0)
    GPIO.setup(echo_pin, GPIO.IN)
}

def start() {
    GPIO.output(trigger_pin, GPIO.HIGH)
    time.sleep(static_time)
    GPIO.output(trigger_pin, GPIO.LOW)
    start_time = getStart(echo_pin)
    end_time = getEnd(echo_pin)
    return [start_time, end_time]
}
def distanceCalc(start_time, end_time) {
    time_duration = start_time - end_time
    distance = time_duration * sound_speed / 2
    return distance
}

def getStart(pin):
    while GPIO.input(pin) == 0:
        start_time = time.time()
    return start_time

def getEnd(pin):
    while GPIO.input(pin) == 1:
        end_time = time.time()
    return end_time

try:
    init()
    time.sleep(2) #Callibrating
    timeArr = start()
    distance = round(distanceCalc(timeArr[0], timeArr[1]), 2)
    self.distance = distance

except KeyboardInterrupt:
    GPIO.cleanup()
