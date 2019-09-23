def arithmetic(a, b, operator):
	operator = {'add': '+', 'subtract': '-', 'divide': '/', 'multiply': '*'}[operator]
	string = str(a)+operator+str(b)
	return eval(string)

'''
def arithmetic(a, b, operator):
    return {
        'add': a + b,
        'subtract': a - b,
        'multiply': a * b,
        'divide': a / b,
    }[operator]



def arithmetic(a, b, operator):
    ops = {"add":"+","subtract":"-","multiply":"*","divide":"/"}
    return eval(str(a)+ops[operator]+str(b))


'''