
import random
import time
import os
import requests
import mechanize

class Transaction(object):
    def __init__(self):
        pass

    def run(self):
        headers = {'Authorization': 'Basic cmVuZGVyZXI6UzU4UmhQNkJCSFBSVlVoNHQza3BvSTBBRzZ6MFh1NjB1SjcybTM5Ug=='}
        start_timer = time.time()
        response = requests.get(url="https://staging.slydes.qubecinema.com/sly-init/render?template_id=cb3b306f-399f-4e73-b490-b47b330b215e&message=Happy birthday")
        latency = time.time() - start_timer
        self.custom_timers["Time_Taken_For_Render_Template_API"] = latency
        #print str(response.status_code) + '--->' + response.content
        assert(response.status_code == 200)
        if(response.status_code!=200):
            print 'Failed Response: --> statuscode : {0} , content : {1}'.format(str(response.status_code),response.content)


if __name__ == '__main__':
    trans = Transaction()
    trans.run()
    print trans.custom_timers
