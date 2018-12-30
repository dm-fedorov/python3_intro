# yahoo_api.py
def get_forecast(city):
    '''
    Запрос погоды в градусах по Фаренгейту с сайта: https://developer.yahoo.com/weather/
    '''
    import requests        
    url = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22{city}%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys'
    try:
        data = requests.get(url.format(city=city)).json()
        forecast = data['query']['results']['channel']['item']['forecast']
        result = []
        for day in forecast:
            result.append({'date': day['date'], 'high_temp': day['high']})
        return result
    except Exception as e:
        return e

if __name__ == '__main__':    
    import pprint
    print('St. Petersburg:')
    pprint.pprint(get_forecast('St. Petersburg'))
    print('Moscow:')
    pprint.pprint(get_forecast('Moscow'))
