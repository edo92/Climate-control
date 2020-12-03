import os
from sensor import Enviro
from util import Request
from src.safety import Safety
import json


class Transmite:
    endpoint = os.getenv('SERVER_URI')

    def __init__(self):
        # Initialize request
        self.request = Request(self.endpoint)

    def get_configs(self):
        res = self.request.get('/configs')
        return json.loads(res.content)

    def on(self, data):
        self.request.post('/climate-data', data)

    def notify(self, data):
        self.post('/notify', data)


class Program:
    def __init__(self):
        # Initialize Enviro board
        self.sensor = Enviro(self.sensor_output)
        # Transmite data
        self.conn = Transmite()
        # Get config instructions
        self.configs = self.conn.get_configs()
        # safety pass jobs(time, function), and configs
        self.safety = Safety(self.configs)

    # Sensor output callback passed to Enviro
    def sensor_output(self, data):
        self.conn.on(data)
        self.safety.on(data)

    def main(self):
        self.safety.start(self.sensor)
        self.sensor.start()


Program().main()
