#Escreva um programa que leia dois números reais e pergunte depois ao utilizador qual a operação aritmética que este deseja realizar e apresente o resultado. 
num1 , opr , num2 = input("Digite 2 números e a operação desejada (+ ; - ; * ; / ), tudo separado por espaço: ").split()
num1=int(num1)
num2=int(num2)

if opr == '+':
        print('{} + {} = '.format(num1, num2))
        print(num1 + num2)

elif opr == '-':
    print('{} - {} = '.format(num1, num2))
    print(num1 - num2)

elif opr == '*':
    print('{} * {} = '.format(num1, num2))
    print(num1 * num2)

elif opr == '/':
    print('{} / {} = '.format(num1, num2))
    print(num1 / num2)

else:
    print('Introduziu algo de errado, execute o programa de novo.')
