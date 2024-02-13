conta = {
    'saldo':1030,
    'transacoes':1,
    'media':203.0
}

def compra(conta, valor):
    if valor > conta['saldo']:
        print("Saldo insufiente para realizar essa transação")
    else:
        conta['transacoes']+=1
        conta['saldo']-=valor
        conta['media']+=valor/conta['transacoes']
    return conta

compra(conta,6000)
print(conta)