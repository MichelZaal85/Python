def rewrite(names):
    if not names:
        return ''
    nameList = []
    if len(names) > 1:
        for dic in range(len(names) - 1):
            nameList.append(names[dic]['name'])
        s = ', '.join(nameList)
        s += ' & ' + names[-1]['name']
        return(s)
    else:
        return(names[0]['name'])

print(rewrite([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Margret'},{'name': 'Homer'}]))
print(rewrite([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Margret'}]))
print(rewrite([{'name': 'Bart'}]))
print(rewrite([]))
