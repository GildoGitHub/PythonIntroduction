#Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores 
#com base em comissões. O vendedor recebe $200 por semana mais 9 por cento de suas vendas
#brutas daquela semana. Por exemplo, um vendedor que teve vendas brutas de $3000 em uma 
#semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470. Escreva um 
#programa (usando um array de contadores) que determine quantos vendedores receberam 
#salários nos seguintes intervalos de valores:$200 - $299 $300 - $399 $400 - $499 
#$500 - $599 $600 - $699 $700 - $799 $800 - $899 $900 - $999 $1000 em diante Desafio: Crie 
#ma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs 
#aninhados.

def salarioTotal(vendedor):
    sal = 200 + (vendedor*0.09)
    return sal

contadorers = [0,0,0,0,0,0,0,0,0,0]

VendA = 5000
vendB = 60075
vendC = 3500
VendD = 1000
VendE = 1000
VendF = 100090

Trabalhadores = [VendA ,vendB, vendC, VendD, VendE, VendF]

for Trabalhador in Trabalhadores:
    tota = salarioTotal(Trabalhador)
    posi = int(tota / 100)-1
    if posi >= 1 and posi <= 9:
        contadorers[posi]+=1
    elif posi > 9:
        contadorers[9]+=1
    

i = 1

print("  Intervalo     Quantidade\n")
while i <= 9:
   if i==9:
       print("[ 1000 -- ++ ]      ",contadorers[i])
   else:
        print("[",((i+1)*100),"--",((i+1)*100)+99,"]      ",contadorers[i])
   i+=1


