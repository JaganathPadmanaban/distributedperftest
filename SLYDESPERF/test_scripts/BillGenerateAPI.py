
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
        response = requests.post(url="https://staging.slydes.qubecinema.com/sly-init/bill", data = '{\
   "templateId": "cb3b306f-399f-4e73-b490-b47b330b215e",\
   "templateData": {\
       "message": "Happy Birthday"\
   },\
   "screenId": "c4e57102-dfce-4bfb-bca4-e49d0a1564a2",\
   "scheduleTime": "2017-08-05T09:30:28.55517Z"\
}')
        latency = time.time() - start_timer
        self.custom_timers["Time_Taken_For_Booking_Slydes"] = latency
        #print str(response.status_code) + '--->' + response.content
        assert(response.status_code == 200)
        if(response.status_code!=200):
            print 'Failed Response: --> statuscode : {0} , content : {1}'.format(str(response.status_code),response.content)


if __name__ == '__main__':
    trans = Transaction()
    trans.run()
    print trans.custom_timers
