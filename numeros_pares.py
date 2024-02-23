#Escreva um programa que recebe uma lista de números do usuário e retorna uma nova lista contendo apenas os números pares da lista original.

#criando lista principal
numeros = []

#coletando dados do usuário

while True:
    n1 = input('Digite um número para a lista (Digite 0 para encerrar o programa): ')

    if n1 == '':
        break

    #convertendo elementos da lista em números inteiros
    inteiro = int(n1)
    numeros.append(inteiro)


#criando lista de pares e condição para analisar elementos da lista principal
i = 0
pares = []
while i < len(numeros):

    #verificando os números pares
    if numeros[i] % 2 == 0:
        pares.append(numeros[i])

    i+=1

print(pares)
