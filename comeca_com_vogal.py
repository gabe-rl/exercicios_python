#Escreva um programa que recebe uma lista de palavras do usuário e retorna uma nova lista contendo apenas as palavras que começam com uma vogal.

#criando e alimentando lista com dados do usuário

lista = []

while True:
    palavra = input('Digite uma palavra para a lista (Digite Enter para encerrar o programa): ').lower()

    if palavra == '':
        print('Programa encerrado. Prosseguindo...')
        break

    
    lista.append(palavra)

#criar nova lista e analisar palavras

vogais = []
i = 0

for palavra in lista:

    if palavra[0] in 'aeiou':

        vogais.append(palavra)
    
    i+=1


print(vogais)