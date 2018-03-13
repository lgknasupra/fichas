#Escreva um programa que leia dois valores numéricos e os apresente do maior para o menor valor.

num1 , num2 = input("Digite 2 números separados por espaço: ").split()

num1 = int(num1)
num2 = int(num2)

if num1 == num2:
    print("Os números que introduziu são iguais. {}".format(num1))
elif num1 > num2:
    print(num1,num2)
else:
    print(num2,num1)