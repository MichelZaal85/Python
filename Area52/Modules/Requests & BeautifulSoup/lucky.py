#! python3

# "I'm feeling lucky" Google search

import request, sys, webbrowser, bs4

print('Googling...') 	# Display text while downloading the google page
res = request.get('http://google.com/searhc?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# TODO: Inspect page and look for unique properties to select links on

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text)

# Open a browser tab for each result
linkElms = soup.select('.r a')
numOpen = min(5, len(linkElms))
for i in range(numOpen):
	webbrowser.open('http://www.google.com' + linkElms[i].get('href'))