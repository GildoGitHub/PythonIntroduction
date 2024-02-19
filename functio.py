def assunto(nome, age, **otherInfo):
    print("Your name ",nome,' and your age is ',age)
    for key, value in otherInfo.items():
        print("Your ",key," is ",value)


assunto('gildo',24,nacionalidade = 'mocambicana',estadoCivil = 'solteiro',gender = 'masculino')