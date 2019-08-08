import requests

class sncf:
    def __init__(self):
        self.token_auth= '07a789e1-cd3c-467a-bf38-0d1259b3afa9'
        self.url = 'https://api.sncf.com/v1'
        self.param1 = '/coverage/sncf/stop_areas/stop_area:OCE:SA:87722025/departures'
        self.trains ={}

    def requetes(self):
        r = requests.get(self.url + self.param1, auth=(self.token_auth, ''))
        self.trains = r.json()

    def get_next_departures(self):
        next_departures = []
        for i in range(0, 10):
            next_departures.append(self.trains['departures'][i]['display_informations']['direction'])
        print(next_departures)
        return next_departures

