#Escreva um programa que recebe duas listas de números do usuário e retorna uma nova lista contendo apenas os números que estão presentes em ambas as listas.

lista_1 = []
lista_2 = []

for i in range (1,4):
    n1 = int(input('Digite um número para a primeira lista: '))
    lista_1.append(n1)

for i in range (1, 4):
    n2 = int(input('Digite um número para a segunda lista: '))
    lista_2.append(n2)


conjunto_1 = set(lista_1)
conjunto_2 = set(lista_2)

inter = conjunto_1 & conjunto_2

inter = list(inter)

print(inter)