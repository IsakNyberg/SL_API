# SL_API
Unofficial python wrapper for the SL API

Get keys from: https://www.trafiklab.se/api/trafiklab-apis/sl/departures-4/

and from: https://www.trafiklab.se/api/trafiklab-apis/sl/stop-lookup/

Installation
------------

Using pip (TODO):

    pip install 

or using setup.py:

    git clone https://github.com/IsakNyberg/SL_API.git
    cd SL_API
    pip install mypackage


Usage

    >>> import sl_api
    >>> sl_stop_lookup_key = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
    >>> sl_departures_key  = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

    >>> station_finder = sl_api.StationFinder(sl_stop_lookup_key)
    >>> station = station_finder.create_station_from_name('Odenplan', sl_departures_key, timewindow=5)

    >>> response = station.request()
    >>> print(response)

Lists all departures of Busses, Trams and Trains from Odenplan in the next 5 min.

