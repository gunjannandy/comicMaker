import requests
from clint.textui import progress

def checkProgress(url,path):
	r = requests.get(url, stream=True)
	with open(path, 'wb') as f:
	    total_length = int(r.headers.get('content-length'))
	    for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1): 
	        if chunk:
	            f.write(chunk)
	            f.flush()