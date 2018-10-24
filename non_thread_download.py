#downloading using single thread
import urllib3
urllib3.disable_warnings()

def download_url(url, file_name):
	print("downloading the content of {} into {}". format(url, file_name))
	http = urllib3.PoolManager()
	response = http.request(method="GET", url=url)
	with open(file_name, "wb") as f:
		f.write(response.data)
	
	print("download of {} complete".format(url))

test_dict = {
	
	"Google":"http://www.google.com",
	"Python":"http://www.python.org",
	"Yahoo":"http://www.yahoo.com",
	"Bing":"http://www.bing.com"
	}
	
for key in test_dict:
	download_url(test_dict[key], key)

	
	
