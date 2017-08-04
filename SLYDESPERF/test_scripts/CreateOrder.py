
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
        response = requests.post(url="https://staging.slydes.qubecinema.com/sly-init/order", data = '{\
    "slydeId" : "8f35df7f-aeb8-49ff-bdc2-84733218447f",\
    "clientReference": "JUSTKT",\
    "user" : {\
        "name": "Meenakshi",\
        "email": "meenakshi@realimage.com",\
        "mobile": "9791043320"\
    }\
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
