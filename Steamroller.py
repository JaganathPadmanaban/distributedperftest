import requests
import time
import threading

class loadrequestget(threading.Thread):

    def __init__ (self, times, url):
        threading.Thread.__init__(self)
        self.times = times
        self.url = url

    def run(self):
        for i in range(1, self.times):
            x = time.time()
            response = requests.get(self.url)
            y = time.time() - x
            print y

            print response.content

def sendload(threadds,ranges,urls):
    threads = []
    for num in range(0, threadds):
        thread = loadrequestget(ranges, urls)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()
        

#sendload(20,10,"https://jt-purchases.herokuapp.com/availability?session_id=95933626-5ace-48ed-b17a-dd09f5bf90bd&channel=JUSTICKETS-WEB")