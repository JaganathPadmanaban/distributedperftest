
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
        response = requests.get(url="https://test.moviebuff.com/mersal.json")
        latency = time.time() - start_timer
        self.custom_timers["Time_Taken_For_loading_movie_json"] = latency
        #print str(response.status_code) + '--->' + response.content
        assert(response.status_code == 200)
        if(response.status_code!=200):
            print 'Failed Response: --> statuscode : {0} , content : {1}'.format(str(response.status_code),response.content)


if __name__ == '__main__':
    trans = Transaction()
    trans.run()
    print trans.custom_timers
