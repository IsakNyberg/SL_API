# SL_API
Unofficial python wrapper for the SL API

Get keys from: https://www.trafiklab.se/api/trafiklab-apis/sl/departures-4/

and from: https://www.trafiklab.se/api/trafiklab-apis/sl/stop-lookup/

Installation
------------

Using pip:

    pip install 

or using setup.py:

    git clone 
    cd 
    python setup.py install


Usage

    >>> import sl_api
    >>> sl_stop_lookup_key = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
    >>> sl_departures_key = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
    
    >>> station_finder = sl_api.StationFinder(sl_stop_lookup_key)
    >>> station = station_finder.create_station_from_name('Odenplan', sl_departures_key, timewindow=5)

    >>> response = station.request()
    >>> print(response)
    
    Lists all departures of Busses, Trams and Trains from Odenplan in the next 5 min.

