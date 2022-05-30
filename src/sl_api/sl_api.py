import requests


class StationFinder:
    url = 'https://api.sl.se/api2/typeahead.json'
    s  = requests.Session()
    def __init__(self, sl_stop_lookup_key, stations_only=True, maxresults=10, type_=None):
        self.key = sl_stop_lookup_key
        self.stations_only = stations_only
        self.maxresults = maxresults
        self.type = type_

    def search_station(self, name):
        method = 'POST'
        url = self.url
        payload = {
            'Key': self.key,
            'SearchString': name,
            'StationsOnly': self.stations_only,
            'MaxResults': self.maxresults
        }
        if self.type != None:
            payload['type'] = self.type
        result = self.s.request(method=method, url=url, params=payload)
        result = result.json(encoding='utf-8')
        if result['StatusCode'] == 0:
            result = result['ResponseData']
        else:
            raise ValueError(result)

        return result

    def create_station_from_name(self, name, sl_api_key, **kwargs):
        search = self.search_station(name)
        best_result = search[0]
        print('Found {0} at x:{1} y:{2} id: {3}'.format(
            best_result['Name'],
            best_result['X'],
            best_result['X'],
            best_result['SiteId'])
        )
        seiteid = int(best_result['SiteId'])

        return Station(sl_api_key, seiteid, **kwargs)


class Station:
    url = 'https://api.sl.se/api2/realtimedeparturesV4.json'
    s  = requests.Session()

    def __init__(self, sl_api_key, station_id, timewindow=60,
            bus=True, metro=True, train=True, tram=True,
            ship=False, enable_prediction=True
        ):
        self.key = sl_api_key
        self.seiteid = station_id
        self.timewindow = timewindow
        self.bus = True
        self.metro = True
        self.train = True
        self.tram = True
        self.ship = False
        self.enable_prediction = True
        self.cashed_request = None

    def format_payoad(self):
        return {
            'Key': self.key,
            'SiteId': self.seiteid,
            'TimeWindow': self.timewindow,
            'Bus': self.bus,
            'Metro': self.metro,
            'Train': self.train,
            'Tram': self.tram,
            'Ship': self.ship,
            'EnablePrediction': self.enable_prediction,
        }

    def request(self):
        method = 'POST'
        url = self.url
        payload = self.format_payoad()
        result = self.s.request(method=method, url=url, params=payload)
        result = result.json(encoding='utf-8')
        self.cashed_request = result
        if result['StatusCode'] == 0:
            result = result['ResponseData']
        else:
            raise ValueError(result)

        return result

    def get_line_by_type(self, line_type):
        if self.cashed_request is None:
            raise ValueError('Make request before reading data')
        valid_types = ['Metros','Buses','Trains','Trams','Ships']
        if line_type not in valid_types:
            raise ValueError(f'Invalid travel type {line_type} must be {valid_types}')

        return self.cashed_request['ResponseData'][line_type]

    def get_line_by_number(self, line_num):
        line_num = str(line_num)  # make number a string
        if self.cashed_request is None:
            raise ValueError('Make request before reading data')
        valid_types = ['Metros','Buses','Trains','Trams','Ships']
        res = {}
        for line_type in valid_types:
            lines = self.cashed_request['ResponseData'][line_type]
            res[line_type] = [line for line in lines if line['LineNumber'] == line_num]

        return res
