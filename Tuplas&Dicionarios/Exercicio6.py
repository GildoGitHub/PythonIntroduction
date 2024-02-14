
def contaVogais(text):
    dicionario = {}
    lista = list(text)
    vogais=['a','e','i','o','u']
    for letra in lista:
        if letra.lower() in vogais:
            if letra.lower() in dicionario.keys():
                dicionario[letra.lower()]+=1
            else:
                dicionario[letra.lower()]=1
    print(dicionario)


contaVogais("maria, gildo, maputo , Ermelinda")