from sensor import Sensor, LCD
from util import Request
from server import Server

import json
import math


class Program:
    endpoint = 'http://192.168.1.243:3000'
    ipAddress = '192.168.1.121'
    port = 80

    def __init__(self):
        # Initialize sensor
        self.sensor = Sensor()
        # Initialize LCD
        self.lcd = LCD()
        # Set request
        self.request = Request(self.endpoint)
        # Get config and instructions from server
        self.get_configs()

    def get_configs(self):
        # Get configs and instructions
        self.config = self.request.get('/config')

    def display_data(self, data):
        temp = data['temperature']
        self.show_data = str(round(temp['data'], 2)) + ' ' + temp['unit']

        self.lcd.contnent(self.show_data)
        self.lcd.text_position()
        self.lcd.draw_display()

    def sensor_output(self, data):
        self.request.post(data=data)
        self.display_data(data)

    def main(self):
        self.sensor.start(self.sensor_output)
        self.lcd.run()


Program().main()
