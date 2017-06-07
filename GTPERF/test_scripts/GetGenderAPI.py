
import random
import time
import os
import requests
import mechanize

class Transaction(object):
    def __init__(self):
        pass

    def run(self):
        start_timer = time.time()
        response = requests.get(url="https://jt-purchases.herokuapp.com/greetings/templates/list?session=1a2357d2-febf-4add-a06a-8a221fc74897&channel=JUSTICKETS-WEB")
        latency = time.time() - start_timer
        self.custom_timers["Time taken for getting List templates"] = latency
        #print str(response.status_code) + '--->' + response.content
        assert(response.status_code == 200)
        if(response.status_code!=200):
            print 'Failed Response: --> statuscode : {0} , content : {1}'.format(str(response.status_code),response.content)


if __name__ == '__main__':
    trans = Transaction()
    trans.run()
    print trans.custom_timers
