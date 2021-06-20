Horas = []

#Pede para o usuario quantas horas deseja converter 
for c in range(0,1):
    Horas.append ( int(input("Digite aqui o valor para converter para segundos: ")) )  

#Transforma a lista em valor "Int"
HorasInt = sum(Horas)

#Converte a hora para segundo
Segundos = HorasInt * 3600

#Imprime os segundos
print(Segundos)