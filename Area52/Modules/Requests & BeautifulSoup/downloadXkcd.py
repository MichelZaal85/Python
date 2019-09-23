#! python3
# downloadXkcd.py -- Downloads every single XKCD comic.

import requests, os, bs4, urllib

url = 'https://loadingartist.com/comic/ive-made-a-huge-mistake/'			# starting url
os.makedirs('loadingArtist', exist_ok=True)	# store comics in ./xkcd

for i in range(25):
	# Download the page
	print('Downloading page %s...' % url)
	# make a request
	res = requests.get(url)
	res.raise_for_status()

	# Get sourcecode of url
	soup = bs4.BeautifulSoup(res.text, 'html.parser')

	# Find the URL of the comic image
	comicElm = soup.select('.comic img')
	if comicElm == []:
		print('Could not find comic image')
	else:
		# write url to comicUrl
		comicUrl = comicElm[1].get('src')

		# Download the image.
		print('Downloading image %s...' % (comicUrl))
		res.raise_for_status()

		# Save the image to ./loadingArtist
		
		comicName = comicUrl.split('/')[-1]
		urllib.request.urlretrieve(comicUrl, './loadingArtist/'+comicName)
		
		# imageFile = open(os.path.join('loadingArtist', os.path.basename(comicUrl)), 'wb')
		# for chunk in res.iter_content(100000):
		# 	imageFile.write(chunk)
		# imageFile.close()

	# Get the Prev button's url.
	nextLink = soup.select('a.ir-random')[0]
	url = 'https://loadingartist.com/' + nextLink.get('href')

print('Done')

