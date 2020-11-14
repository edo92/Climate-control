from util import Moment
import schedule


class Job_Schedule:
    def __init__(self):
        self.schedule = schedule

    def isBetween(self, start, end):
        return Moment.isBetween(start, end)

    def set_schedule(self, time, action):
        self.schedule.every().day.at(time).do(action)
        self.schedule.run_pending()

    def create_job(self, action, start, end):
        self.set_schedule(start, action)
        if self.isBetween(start, end) == True:
            action()

    def schedule_job(self, config, jobs_list):
        for job in jobs_list:
            start = job[0][0]
            end = job[0][1]
            actions = job[1]
            for action in actions:
                self.create_job(action, start, end)

    def on(self):
        self.schedule.run_pending()
