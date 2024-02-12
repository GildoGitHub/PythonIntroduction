agenda = {}

def incluirNovoNome(nome,*phones):
    lista=[]
    for phone in phones:
        lista.append(phone)
    agenda[nome]=lista

incluirNovoNome('Gildo','8433','8888','9485','77565')

print(agenda)

def incluirTelefone(nome, telefone):
    if nome in agenda:
        agenda[nome].append(telefone)
    else:
        value = input("Deseja incluir um novo contacto? Insira S para sim ou outro caracter para não: ")
        if value.upper() == 'S':
            incluirNovoNome(nome,telefone)


incluirTelefone('Maria','999')
incluirTelefone('Marta','989')
incluirTelefone('Maico','111')
incluirTelefone('Maico','116')
incluirTelefone('Marta','949')

print()
print(agenda)
print()

def excluirTelefone(nome, telefone):
    if nome in agenda and telefone in agenda[nome]:
            if len(agenda[nome])==1:
                excluirNome(nome)
            else:
                agenda[nome].remove(telefone)
    else:
        print("We don't have this contact name or this phone number\n")       


excluirTelefone('Marta','989')

print(agenda)

def excluirNome(nome):
    if nome in agenda:
        del agenda[nome]
    else:
        print('Esta pessoa não existe na agenda\n')


excluirNome('joao')

def consultarTelefone(nome):
    contactos = []
    if nome in agenda:
       contactos = agenda[nome]
    return contactos

nomeConsulta = input('Insira um nome porfavor: ')

listaContactos = consultarTelefone(nomeConsulta)

if listaContactos:
    print(listaContactos)
else:
    print('NAO EXISTE ESSE CONTACTO')