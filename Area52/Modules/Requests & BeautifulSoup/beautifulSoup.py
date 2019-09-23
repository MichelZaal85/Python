import requests, bs4

# Creating a BeautifulSoup Object from HTML
res = requests.get('http://nostarch.com')
res.raise_for_status()

# noStarchSoup = bs4.BeautifulSoup()
# print('Type:', type(noStarchSoup))

# Loading file into bs4 object
exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile, 'html.parser') # without 'html.parser', warning
print('Type:', type(exampleSoup))

# CSS Selectors:

exampleSoup.select('div')						# All elements named div
exampleSoup.select('#author')					# id selector
exampleSoup.select('.notice')					# class selector
exampleSoup.select('div span')					# span within div
exampleSoup.select('div > span')				# direct child of div
exampleSoup.select('input[name]')				# input elements with name attribute
exampleSoup.select('input[type="button"]')		# input elements with type value button


# Example of above selectors
exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read())
elems = exampleSoup.select('#author')
type(elems)
# <class 'list'>
len(elems)
# 1
type(elems[0])
# <class 'bs4.element.Tag'>
elems[0].getText()
# 'Al Sweigart'
str(elems[0])
# '<span id="author">Al Sweigart</span>'
elems[0].attrs
# {'id': 'author'}


soup = bs4.BeautifulSoup(open('example.html'))
spanElm = soup.select('span')[0]
print(str(spanElm))

spanElm.get('id')

spanElm.get('Some_nonexistent_addr') == None

print(spanElm.attrs)


