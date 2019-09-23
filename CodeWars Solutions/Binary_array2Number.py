# Return the int from the binary array


def binary_array_to_number(arr):
    return int(''.join(str(n) for n in arr), 2)


'''
# alternative solutions
def binary_array_to_number(arr):
  return int("".join(map(str, arr)), 2)

def binary_array_to_number(arr):
    append_bit = lambda n, b: n << 1 | b
    return reduce(append_bit, arr)
'''


# tests
binary_array_to_number([0, 0, 0, 1])                    # ==> 1
binary_array_to_number([0, 0, 1, 0])                    # ==> 2
binary_array_to_number([1, 1, 1, 1])                    # ==> 15
binary_array_to_number([0, 1, 1, 0])                    # ==> 6
binary_array_to_number([1, 1, 0, 1, 0, 1, 1, 0, 0, 0])  # ==> 856
binary_array_to_number([1, 1, 1, 0, 1, 1, 1, 1, 1, 1])  # ==> 959
binary_array_to_number([1, 1, 1, 0, 1, 0, 0, 1, 0, 1])  # ==> 933
binary_array_to_number([1, 0, 1, 0, 0, 0, 1, 0, 1])     # ==> 325
binary_array_to_number([1, 1, 0, 1, 0, 1, 0])           # ==> 106
binary_array_to_number([1, 0, 1, 0, 1, 1, 0, 1, 1, 0])  # ==> 694
binary_array_to_number([1, 0, 0, 0, 1, 0, 1, 0, 1, 1])  # ==> 555
binary_array_to_number([1, 0, 0, 1, 0, 1, 0, 0, 1])     # ==> 297
binary_array_to_number([1, 1, 1, 1, 1, 0, 0, 0, 0])     # ==> 496
binary_array_to_number([1, 0, 1, 0, 1, 1, 0, 0, 1])     # ==> 345
binary_array_to_number([1, 0, 1, 1, 0, 1, 0, 1, 1])     # ==> 363
binary_array_to_number([1, 1, 1, 0, 0, 0, 1, 1, 0])     # ==> 454
binary_array_to_number([1, 0, 1, 1, 1, 0, 0, 0, 1])     # ==> 369
binary_array_to_number([1, 0, 1, 1, 1, 1, 1, 1, 1, 0])  # ==> 766
binary_array_to_number([1, 0, 0, 0, 0, 1, 1])           # ==> 67
binary_array_to_number([1, 1, 1, 1, 0, 0, 1, 1, 0, 0])  # ==> 972
binary_array_to_number([1, 0, 1, 1, 0, 0, 0, 1, 0, 0])  # ==> 708
binary_array_to_number([1, 1, 0, 1, 1, 1, 1, 0, 0, 1])  # ==> 889
binary_array_to_number([1, 0, 0, 1, 0, 1, 1, 0, 1, 0])  # ==> 602
binary_array_to_number([1, 1, 0, 0, 1, 1, 1, 0, 0, 1])  # ==> 825
binary_array_to_number([1, 1, 1, 0, 0, 0, 1, 1, 1, 1])  # ==> 911
binary_array_to_number([1, 0, 1, 1, 0, 0, 0, 0, 0])     # ==> 352
binary_array_to_number([1, 0, 1, 0, 0, 0, 0, 1, 0, 1])  # ==> 645
binary_array_to_number([1, 0, 1, 0, 1, 0, 1, 1, 1, 0])  # ==> 686
binary_array_to_number([1, 1, 1, 0, 1, 0, 0, 1])        # ==> 233
binary_array_to_number([1, 1, 0, 1, 0])                 # ==> 26
binary_array_to_number([1, 1, 1, 0, 0, 0, 0])           # ==> 112
binary_array_to_number([1, 1, 0, 0, 0, 0, 1, 1, 1, 1])  # ==> 783
binary_array_to_number([1, 1, 1, 0, 1, 1, 0, 0, 0, 1])  # ==> 945
binary_array_to_number([1, 1, 1, 0, 1, 0, 0, 0, 1, 0])  # ==> 930
binary_array_to_number([1, 1, 0, 1, 1, 1, 1, 0, 1])     # ==> 445
binary_array_to_number([1, 1, 1, 0, 0, 1, 0, 0, 0, 1])  # ==> 913
binary_array_to_number([1, 0, 1, 0, 0, 0, 1, 1])        # ==> 163
binary_array_to_number([1, 1, 1, 0, 0, 1, 0, 0, 1, 1])  # ==> 915
binary_array_to_number([1, 0, 1, 1, 0, 0, 0, 1, 1])     # ==> 355
binary_array_to_number([1, 0, 0, 1, 1, 1])              # ==> 39
binary_array_to_number([1, 0, 0, 0, 0, 0, 1])           # ==> 65
binary_array_to_number([1, 0, 0, 0, 1, 0, 0, 0])        # ==> 136
binary_array_to_number([1, 0, 1, 0, 1, 0, 0, 1, 0, 0])  # ==> 676
binary_array_to_number([1, 0, 1, 0, 0, 1, 1, 1, 0, 1])  # ==> 669
binary_array_to_number([1, 0, 0, 0, 0, 0, 1, 1])        # ==> 131
binary_array_to_number([1, 0, 0, 1, 1, 0, 0, 1])        # ==> 153
binary_array_to_number([1, 0, 1, 1, 0, 0, 0, 0, 1, 0])  # ==> 706
binary_array_to_number([1, 1, 1, 0, 1, 0, 1, 0, 0, 1])  # ==> 937
binary_array_to_number([1, 1, 1, 1, 1, 1, 1, 1, 0])     # ==> 510
binary_array_to_number([1, 0, 0, 1, 0, 1, 0, 1, 0])     # ==> 298
binary_array_to_number([1, 0, 0, 0, 1, 0, 1, 0, 0])     # ==> 276
binary_array_to_number([1, 0, 0, 1, 0, 1, 0, 0, 1, 0])  # ==> 594
binary_array_to_number([1, 1, 0, 0, 0, 0, 0, 1, 1, 0])  # ==> 774
binary_array_to_number([1, 1, 0, 0, 0, 1, 1, 0, 1, 0])  # ==> 794
