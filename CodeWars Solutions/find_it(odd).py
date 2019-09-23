'''
    Codewars, find the odd number in the sequence
'''


def find_it(seq):
    for i in seq:
        if seq.count(i) % 2:
            return(i)


# similar solutions:

def find_it(seq):
    return [x for x in seq if seq.count(x) % 2][0]
