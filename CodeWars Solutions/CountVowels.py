def getCount(inputStr):
    count = 0
    vowels = ['a', 'e', 'i', 'u', 'o']
    for vowel in vowels:
        if vowel in inputStr:
            count += 1
    return count


# def getCount(inputStr):
#     return sum(1 for let in inputStr if let in "aeiouAEIOU")
