# '''

# Write a function that returns the count of characters that have to be removed
# in order to get a string with no consecutive repeats.

# Note: This includes any characters

# Examples

# 'abbbbc'  => 'abc'    #  answer: 3
# 'abbcca'  => 'abc'    #  answer: 2
# 'ab cca'  => 'ab ca'  #  answer: 1
# '''


# def count_repeats(txt):
#     i = 0
#     t = ''
#     txt = txt.lower()
#     for c in txt:
#         if txt.count(c) >= 2 and c != t:
#             i += 1
#             t = c
#     return i


# print(count_repeats('AaBbbCCC'))
# print(count_repeats('abbc'))  # 1
# print(count_repeats('abbcca'))  # 2
# print(count_repeats('ab cca'))  #  1


def repeats(txt):
    t = ''
    i = 0
    new_list = []
    txt = [i for i in txt]
    for c in txt:
        if c != t:
            new_list.append(c)
            i += 1
        t = c
    return 'New List:', ''.join(new_list), 'Deleted:', i


print(repeats('abbbbc'))
print('\n')
print(repeats('abb bbc'))
print(repeats('ab cca'))
