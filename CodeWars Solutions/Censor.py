def censor(text,word):
	for i in text.split():
		if word in text:
			text.replace(word, "*" * len(word)

censor("what the hack is hack here hack", "hack")