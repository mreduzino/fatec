def classificar_idade(nome, idade):
    if idade >= 65:
        return f"Bem-vindo {nome}, você é maior de 65 anos."
    elif idade >= 18:
        return f"Bem-vindo {nome}, você é maior de idade."
    else:
        return f"Bem-vindo {nome}, você é menor de idade."

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

print(classificar_idade(nome, idade))
