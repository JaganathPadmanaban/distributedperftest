
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
        response = requests.get(url="https://mb-schedules-staging.herokuapp.com/movies?token=Xa93HSexxAR73uGfMNYLjJ6F6npWdm&theater=bd4336ba-0c22-4978-826b-fb35e6b33fc9")
        latency = time.time() - start_timer
        self.custom_timers["Time_taken_for_getting_Movie_information"] = latency
        #print str(response.status_code) + '--->' + response.content
        assert(response.status_code == 200)
        if(response.status_code!=200):
            print 'Failed Response: --> statuscode : {0} , content : {1}'.format(str(response.status_code),response.content)


if __name__ == '__main__':
    trans = Transaction()
    trans.run()
    print trans.custom_timers
