from src.scheduler import Job_Schedule


class Safety_Mechanism:
    def light_state_on(self):
        self.light_state = True

    def light_state_off(self):
        self.light_state = False

    def light_safety(self, data):
        lux = data['lux']['data']
        if self.light_state == True and lux == 0:
            print('error')

        if self.light_state == False and lux > 0:
            print('second error')

    def data_safety(self, data, limits):
        def test_limit(data_key, data_point, max_limit, min_limit):
            if data_point > max_limit:
                print(data_key)
                print('is over the limit')

            if data_point < min_limit:
                print(data_key)
                print('is below the limit')

        for data_key in limits:
            for point in limits[data_key]:
                data_point = data[data_key]['data']
                max_limit = limits[data_key]['max']
                min_limit = limits[data_key]['min']
                test_limit(data_key, data_point,
                           max_limit, min_limit)

    def listen(self, configs, data):
        # Listen to data change
        limits = configs['limits']
        self.data_safety(data, limits)
        self.light_safety(data)


class Safety:
    def __init__(self, configs):
        # Initialize modules
        self.configs = configs
        self.job = Job_Schedule()
        self.safety = Safety_Mechanism()

    def start(self, board):
        # Get lighting schedule (timeing)
        config = self.configs['lighting']
        # Pass config and actions to schedule_job
        self.job.schedule_job(config, [
            ((config['on'], config['off']),
             [board.lcd.run, self.safety.light_state_on]),

            ((config['off'], config['on']),
             [board.lcd.stop, self.safety.light_state_off])
        ])

    def on(self, data):
        self.safety.listen(self.configs, data)
        self.job.on()
