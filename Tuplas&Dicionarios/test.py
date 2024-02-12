ola = {
    'Gildo':['893','123']
}

def teste(nome,telefone):
    if nome in ola and telefone in ola[nome]:
        print('Yes')

teste('Gildo','123')