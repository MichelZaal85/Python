# create phonenumber
def create_phone_number(n):
    n = ''.join(str(n) for n in n)
    return f'test: ({n[:3]}) {n[3:6]}-{n[6:]}'


'''
# alternatives
def create_phone_number(n):
  return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)
'''
