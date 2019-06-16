# THIS IS FOR A PROGRESSBAR USING "PROGRESS" ->

from clint.textui import progress
import requests

def checkProgress(url,path):
	try:
		r = requests.get(url, stream=True, headers={'User-Agent': 'Chrome'})
	except:
		checkProgress(url,path)
		return
	else:
		with open(path, 'wb') as f:
		    total_length = int(r.headers.get('content-length'))
		    for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1): 
		        if chunk:
		            f.write(chunk)
		            f.flush()

# THIS IS FOR ANOTHER PROGRESSBAR USING "TQDM" ->

'''
import requests,tqdm,math
def checkProgress(url,path):
	r = requests.get(url, stream=True)

	# Total size in bytes.
	total_size = int(r.headers.get('content-length', 0)); 
	block_size = 1024
	wrote = 0 
	with open(path, 'wb') as f:
	    for data in tqdm.tqdm(r.iter_content(block_size), total=math.ceil(total_size//block_size) , unit='KB', unit_scale=True):
	        wrote = wrote  + len(data)
	        f.write(data)
	        # f.flush()
'''