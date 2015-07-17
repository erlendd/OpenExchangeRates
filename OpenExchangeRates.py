
import urllib2
import json
import time
from decimal import Decimal

class Rates:


    def __init__(self, base, to, apikey):
        self.base = base
        self.to = to
        self.apikey = apikey
        self.lastdownload = 0
        self.dlfreq = 60*60 # 1 hr

        status = self.downloadRates()
        if status: self.validatePairs()

    def timeSinceUpdate(self):
        return time.time() - self.lastdownload

    def validatePairs(self):
        try:
            self.rates[self.to]
            self.rates[self.base]
        except KeyError:
            print 'Invalid base or to currency code'

    def downloadRates(self):
        try:
            resp = urllib2.urlopen('https://openexchangerates.org/api/latest.json?app_id='+self.apikey)
            data = resp.read()
            j = json.loads(data)
            self.rates = j['rates']
            self.lastdownload = time.time() # unixtime
            return True
        except:
            print 'Error updating rates info'
            return False

    def convert(self, amount):
        if time.time() - self.lastdownload > self.dlfreq:
            status = self.downloadRates()
        base_rate = Decimal(str(self.rates[self.base]))
        to_rate = Decimal(str(self.rates[self.to]))
        return Decimal(str(amount)) * to_rate/base_rate



