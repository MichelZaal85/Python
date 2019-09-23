import math
def reverse(n):
    """Returns n with all digits reversed. Assume positive n."""
    if n > 0:
        l = []
        d = 10 ** int(math.log10(n))
        l.append(str(n // d))
        # n =- d *
        return reverse(n)
    else:
        return l

