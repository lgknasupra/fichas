#Ex4
x , y = input("Digite 2 coordenadas (x y) separados por espaço: ").split()

x=int(x)
y=int(y)

if x == 0 and y == 0:
    print("O ponto que introduziu encontra-se na orgiem do referencial.")
elif y == 0:
    print("O ponto que introduziu encontra-se no eixo das abcissas. ")
elif x == 0:
    print("O ponto que introduziu encontra-se no eixo das ordenadas. ")
elif y < 0 and x > 0:
    print("O ponto que introduziu encontra-se no 4º Quadrante ")
elif x < 0 and y > 0:
    print("O ponto que introduziu encontra-se no 2º Quadrante ")
elif y < 0 and x < 0:
    print("O ponto que introduziu encontra-se no 1º Quadrante ")
elif y > 0 and x > 0:
    print("O ponto que introduziu encontra-se no 3º Quadrante ")
