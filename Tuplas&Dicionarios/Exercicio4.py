notas = {
}

def lerDados(notas):
    while True:
        nome = input("Insira nome de um aluno, Insira oooo para terminar: ")
        if nome.lower()=='oooo':
            break
        else:
            nota = int(input("Insira nota do aluno "+nome+": "))
            notas[nome]=nota

lerDados(notas)

def maiorNota(notas):
    nomeMaior = []
    if notas:
        maior = 0
        i=1
        for nome, nota in notas.items():
            if i==1:
                maior=nota
                nomeMaior.append(nome)
            else:
                if nota >= maior:
                    if nota > maior:
                        while nomeMaior:
                            nomeMaior.pop()
                    maior = nota
                    nomeMaior.append(nome)
            i+=1
        
    else:
        print("O dicionario nao contem registos")
    return nomeMaior

print(maiorNota(notas))