notas={}

def notasAluno():
    while True:
        nome = input("\nEscreva o nome do aluno: ")
        if nome:
            notas[nome] = []
            nota = int(input("Insira nota do aluno "+nome+": "))
            notas[nome].append(nota)
            nota = int(input("Insira nota2 do aluno "+nome+": "))
            notas[nome].append(nota)
        else:
            break 

notasAluno()
print(notas)

def mediaNome(nome):
    soma = 0.0
    soma = sum(notas[nome])
    soma/=2
    return soma

nome = input("Insert the name to see the average: ")

if nome not in notas:
    print("The nome don't exist in dictinary")
else:
    print(mediaNome(nome))


def mediaMaior():
    maior = 0
    name = ''
    i=1
    for key in notas.keys():
        med = mediaNome(key)
        if i==1:
            maior = med
            name = key
        else:
            if med > maior:
                maior = med
                name = key
        i+=1
    print(name,"tem media maior que é: ",maior)

mediaMaior()