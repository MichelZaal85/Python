# Description:
# Given an array (arr) as an argument complete the function countSmileys that should return the total number of smiling faces.

# Rules for a smiling face:
# -Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
# -A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
# -Every smiling face must have a smiling mouth that should be marked with either ) or D.
# Valid smiley face examples:
# :) :D ;-D :~)
# Invalid smiley faces:
# ;( :> :} :] 


import re
def count_smileys(arr):
	counter = 0
	for smile in arr:
		if smile.find(')') != -1:
			print(smile)
			counter += 1
		elif smile.find('o') == 1:
			pass
		elif smile.find('D') != -1:
			print(smile)
			counter += 1
	print(counter)


# from re import *

from re import findall
def count_smileys(arr):
	return len(list(findall(r"[:;][-~]?[)D]", " ".join(arr))))

# m = re.match(r'(;|:)(\~|\-)?(\)|D)', x)

count_smileys([]) # should return 0
print()
count_smileys([':)', ';(', ';}', ':-D']);       # should return 2;
print()
count_smileys([';D', ':-(', ':-)', ';~)']);     # should return 3;
print()
count_smileys([';]', ':[', ';*', ':$', ';-D',':oD','Hello']); # should return 1;
