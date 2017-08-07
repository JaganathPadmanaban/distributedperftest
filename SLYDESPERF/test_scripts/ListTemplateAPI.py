
import random
import time
import os
import requests
import mechanize

class Transaction(object):
    def __init__(self):
        pass

    def run(self):
        headers = {'Authorization': 'Basic SlVTVEtUOjJuV29GNnZSbjhrVTl1Z2ZwWlBhaDMzZGRmVmFOdXB1'}
        start_timer = time.time()
        response = requests.get(url="https://staging.slydes.qubecinema.com/sly-init/template/list?screen=28056b51-ce34-49b1-9999-90b1acea617e&time=2017-08-05T17:30:28.55517Z")
        latency = time.time() - start_timer
        self.custom_timers["Time_Taken_For_List_Template_API"] = latency
        #print str(response.status_code) + '--->' + response.content
        assert(response.status_code == 200)
        if(response.status_code!=200):
            print 'Failed Response: --> statuscode : {0} , content : {1}'.format(str(response.status_code),response.content)


if __name__ == '__main__':
    trans = Transaction()
    trans.run()
    print trans.custom_timers
