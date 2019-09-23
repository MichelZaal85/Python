# requests

import requests
res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')

if res.status_code == requests.codes.ok:
	print(res.content[:250])

# Raise err if 404 is given, chrashes the program
print('\n\n')
res.raise_for_status()
print(res.content[:250])


print('\n\n')
res = requests.get('http://inventwithpython.com/page_that_does_not_exist')
try:
	res.raise_for_status()
except Exception as exc:
	print('There was a problem: %s' % (exc))


# Download a file

# get download location
res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
res.raise_for_status()

# setup a binary writable destination, even if plain text!
playFile = open('RomeoAndJuliet.txt', 'wb')

# Download and write per chunk, in this case 100 Kb
# the iter_content() returns chunks of bytes
for chunk in res.iter_content(100000):
	playFile.write(chunk)
playFile.close()
