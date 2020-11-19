import requests
import datetime
import json
import datetime


class Request:
    def __init__(self, url):
        self.url = url
        self.headers = {
            'Content-type': 'application/json',
            'Accept': 'text/plain'
        }

    def get(self, route):
        return requests.get(url=self.url + route, headers=self.headers)

    def post(self, route, data):
        requests.post(url=self.url + route, data=json.dumps(
            data), headers=self.headers)


class Moment:
    @staticmethod
    def isBetween(st, en):
        def parse(st, i):
            return int(st.split(':')[i])

        def format(data):
            formated = str(data).split()[0]
            return int(formated)

        def current_time():
            now = str(datetime.datetime.now().time())
            hour = parse(now, 0)
            minutes = parse(now, 1)
            return datetime.time(hour, minutes)

        def converter(s, e):
            start = (format(parse(s, 0)), format(parse(s, 1)))
            end = (format(parse(e, 0)), format(parse(e, 1)))

            return (datetime.time(start[0], start[1]), datetime.time(end[0], end[1]))

        def time_in_range(start, end, x):
            if start <= end:
                return start <= x <= end
            else:
                return start <= x or x <= end

        start, end = converter(st, en)
        now = current_time()
        return time_in_range(start, end, now)
