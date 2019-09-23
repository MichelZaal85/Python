def int_2_bin(num):
    if num:
        return '0'+bin(num).replace('0b', '')
    return '0'