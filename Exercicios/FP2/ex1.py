#Escreva um programa que leia dois números inteiros e escreva o maior deles.
num1 , num2 = input("Digite 2 números separados por espaço: ").split()

num1 = int(num1)
num2 = int(num2)

if num1 == num2:
    print("Os números que introduziu são iguais. {}".format(num1))
elif num1 > num2:
    print("O maior número é {}".format(num1))
else:
    print("O maior número é {}".format(num2))
