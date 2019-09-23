import re


def validPhoneNumber(phoneNumber):
    print(phoneNumber)
    regex = r'(?!\w)(\(\d{3}\)\s\d{3}-\d{4})(?!\w)'
    if re.findall(regex, phoneNumber):
        return True
    return False

# validPhoneNumber("(123) 456-7890")  =>  returns true
# validPhoneNumber("(1111)555 2345")  => returns false
# validPhoneNumber("(098) 123 4567")  => returns false




# import re
# prog = re.compile('^\(\d{3}\) \d{3}-\d{4}$')
# def validPhoneNumber(phone_number):
#     return prog.match(phone_number) is not None