from pandas import DataFrame
from json import loads
from requests import get
from datetime import datetime
from pytz import timezone

yahoo_headers = {
    'authority':'query1.finance.yahoo.com',
    'origin':'https://finance.yahoo.com',
    'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Mobile Safari/537.36'
}

def get_prices(self, ticker, start_date = None, end_date = None, interval = "1m"):

    #### End Date
    if end_date is None:
        end_date = int(datetime.timestamp(datetime(datetime.now().year, datetime.now().month, datetime.now().day, datetime.now().hour, datetime.now().minute)))
    else:
        end_date = int(datetime.timestamp(datetime.strptime(str(end_date), '%Y-%m-%d')))

    #### Start Date
    if start_date is None:
        start_date = end_date - 60*60*24
    else:
        start_date = int(datetime.timestamp(datetime.strptime(str(start_date), '%Y-%m-%d')))

    if start_date == end_date:
        end_date = start_date + 60*60*24
    

    res = get("https://query1.finance.yahoo.com/v8/finance/chart/{}?period1={}&period2={}&interval={}&includePrePost=true&events=div%7Csplit%7Cearn&&lang=en-US&region=US".format(ticker, str(start_date), str(end_date + 60), interval), headers = yahoo_headers)

    quotes = DataFrame.from_dict(loads(res.content.decode('utf-8')).get('chart').get('result')[0].get('indicators').get('quote')[0])
    quotes['timestamp'] = DataFrame.from_dict(loads(res.content.decode('utf-8')).get('chart').get('result')[0].get('timestamp'))
    quotes = quotes[['timestamp', 'close', 'low', 'open', 'volume', 'high']]
    quotes['timestamp'] = quotes['timestamp'].apply(lambda x: datetime.fromtimestamp(x))
    quotes['timestamp_eastern'] = quotes['timestamp'].apply(lambda x: x.replace(tzinfo=timezone('UTC')).astimezone(timezone('US/Eastern')))
    quotes = quotes[quotes['volume'] != 0]
    
    return quotes[['timestamp', 'timestamp_eastern', 'close', 'low', 'open', 'volume', 'high']]