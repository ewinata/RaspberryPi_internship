import urllib, json, sys


def internet_on():
    '''Checks if network is connected
       returns - True if network is available
    '''
    try:
        with open('./config/config.json', 'r') as conf:
            config = json.load(conf)
        urllib.request.urlopen(config["NETWORK"]["GOOGLE_IP"], timeout=1)
        return True
    except urllib.request.URLError as err: 
        return False
