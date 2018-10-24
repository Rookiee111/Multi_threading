#In this we are going download content from multiple websites using python. However we are going to do so using multiple threads
import urllib3
import threading
urllib3.disable_warnings()

def threaded_download(url, file_name):
	
	print("downloading from {} writing to {} using thread {}".format(url, file_name, threading.current_thread().name))
	http = urllib3.PoolManager()
	response = http.request(method="GET", url=url)
	
	with open(file_name, "wb") as f:
		f.write(response.data)
	
	print("download of {} complete.".format(url))

threads = []
test_dict = {
	
	"Google":"http://www.google.com",
	"Python":"http://www.python.org",
	"Yahoo":"http://www.yahoo.com",
	"Bing":"http://www.bing.com"
	}

print("Starting the execution of main thread ... ")

for key in test_dict:
	thread = threading.Thread(target=threaded_download, name=key, args=(test_dict[key], key))
	threads.append(thread)
	thread.start()

print("Continuing with the execution of main thread by joining the threads")

for thread in threads:
	thread.join()

print("exiting main thread")
