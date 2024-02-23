#Escreva um programa que recebe uma lista de strings do usuário e retorna uma nova lista contendo apenas as strings que têm mais de 5 caracteres.

import os
os.system('cls')

#inicializando lista e coletando dados do usuário

lista = []

while True:
    palavra = input('Digite uma palavra ou Enter para encerrar: ')

    lista.append(palavra)

    if palavra == '':
        print('Dados coletados. Prosseguindo...')
        break


#verificando palavras com mais de 5 caracteres

maiores_5 = []

for palavra in lista:

    if len(palavra) >= 5:
        maiores_5.append(palavra)

print(maiores_5)