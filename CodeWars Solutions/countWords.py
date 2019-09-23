name = raw_input('Enter file, please')
handle = open(name, 'r')
text = handle.read
words = text.split()
count = dict()
for word in words:
	counts[word] = counts.get(word,0)

bigcount = None
bigword = None

for word,count in counts.items():
	if bigcount is None or count > bigcount:
		bigword = word
		bigcount = count

print bigword, bigcount