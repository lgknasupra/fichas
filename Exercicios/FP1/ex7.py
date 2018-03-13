print("Para calcular a duração do album com 5 músicas insira as suas durações.")
print("Musica 1") #musica1
minutos1=int(input("Minutos: "))
segundos1=int(input("Segundos: "))
print("Musica 2") #musica2
minutos2=int(input("Minutos: "))
segundos2=int(input("Segundos: "))
print("Musica 3") #musica3
minutos3=int(input("Minutos: "))
segundos3=int(input("Segundos: "))
print("Musica 4") #musica4
minutos4=int(input("Minutos: "))
segundos4=int(input("Segundos: "))
print("Musica 5") #musica5
minutos5=int(input("Minutos: "))
segundos5=int(input("Segundos: "))

minutost=(minutos1+minutos2+minutos3+minutos4+minutos5)*60
segundost=(segundos1+segundos2+segundos3+segundos4+segundos5)
tempot=(minutost+segundost)

album_horas=tempot//3600
album_minutos=(tempot%3600)//60
album_segundos=(tempot%3600)%60

print("Duração: ",album_horas,":",album_minutos,":",album_segundos)
