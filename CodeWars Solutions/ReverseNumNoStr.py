'''Reverse given number without the string function'''

def reverse(n):
    r = 0
    while n != 0:
        i = n % 10 # get last number
        r = r * 10 + i # some magic
        n //= 10 # chop off last num
    return r




# Other given solutions:
def reverse(n):
    r = 0
    while n:
        r = r*10 + n%10
        n //= 10
    return r

def reverse(n):
    """Returns n with all digits reversed. Assume positive n."""
    rev = lambda n, r: rev(n // 10, 10 * r + n % 10) if n > 0 else r
    return rev(n, 0)

def reverse(n, r=0):
    return reverse(n // 10, r * 10 + n % 10) if n else r