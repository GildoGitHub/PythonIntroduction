d ={
    2:1,
    1:2
}

def inva(d):
    newD = {}
    if d:
        for key, value in d.items():
            if value in newD.keys():
                newD[value]+=[key]
            else:
                newD[value]=[]
                newD[value]+=[key]
    print(newD)

inva(d)