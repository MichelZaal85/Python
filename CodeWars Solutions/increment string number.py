import re

def increment_string(string):
	regex = r"([0-9]+)$"
	match = re.findall(regex, string)
	if match:
		string = re.sub(regex, str(int(match[0])+1), string)
		return string
	else:
		return (string+str(1))

print(increment_string('hello123'))
print(increment_string('hello'))

print(increment_string("foo"))			#  "foo1"
print(increment_string("foobar001"))	#  "foobar002"
print(increment_string("foobar1"))		#  "foobar2"
print(increment_string("foobar00"))	#  "foobar01"
print(increment_string("foobar99"))	#  "foobar100"
print(increment_string("foobar099"))	#  "foobar100"
print(increment_string("")	)		#  "1"
