
def rank(st, we, n):
    li = []
    if len(st) < 1:
        return 'No participants'
    st = st.split(',')
    if len(st) < n:
        return 'Not enough participants'

    for name in st:
        s = 0
        for c in name.lower():
            s += ord(c) % 96
        s += len(name)
        s = s * we[st.index(name)]
        # print(f'{name} \t\t{s * we[st.index(name)]}')
        li.append(s)
    li, st = zip(*sorted(zip(li, st), reverse=True))
    return st[n-1]


print(rank("COLIN,AMANDBA,AMANDAB,CAROL,PauL,JOSEPH",
           [1, 4, 4, 5, 2, 1], 4))


print(rank("Addison,Jayden,Sofia,Michael,Andrew,Lily,Benjamin", [4, 2, 1, 4, 3, 1, 2], 4))
print(rank("Lagon,Lily", [1, 5], 2))
print(rank("Addison,Jayden,Sofia,Michael,Andrew,Lily,Benjamin", [4, 2, 1, 4, 3, 1, 2], 8))
print(rank("", [4, 2, 1, 4, 3, 1, 2], 6))
