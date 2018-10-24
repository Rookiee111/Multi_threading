#implementing the multi thread download using class 
import urllib3
from threading import Thread
urllib3.disable_warnings()

class urlDownload(Thread):
	
	def __init__(self, url, file_name):
		Thread.__init__(self)
		self.url = url
		self.file_name = "Thread_" + file_name
	
	def run(self):
		print("downloading the content of {} into {}".format(self.url, self.file_name))
		http = urllib3.PoolManager()
		response = http.request(method="GET", url=self.url)
		
		with open(self.file_name, "wb") as f:
			f.write(response.data)
		
		print("download of {} complete.".format(self.url))

threads = []
test_dict = {
	
	"Google":"http://www.google.com",
	"Python":"http://www.python.org",
	"Yahoo":"http://www.yahoo.com",
	"Bing":"http://www.bing.com"
	}

print("starting the execution of the Main thread...")
for key in test_dict:
	thread = urlDownload(test_dict[key], key)
	threads.append(thread)
	thread.start()

print("continuing with the main execution  by joining the threads")

for thread in threads:
	thread.join()

print("exiting the Main thread")
