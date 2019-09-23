def up_array(arr):
    if not arr:
        return None
    for i in arr:
        if i < 0 or i > 9:
            return None
    s = ''
    l = []
    for n in arr:
        s += str(n)
    for x in str(int(s) + 1):
        l.append(int(x))
    return(l)


def up_array(arr):
    if not arr or min(arr) < 0 or max(arr) > 9:
        return None
    else:
        return [int(y) for y in str(int("".join([str(x) for x in arr])) + 1)]
