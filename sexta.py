Horas = []

for c in range(0,1):
    Horas.append ( int(input("Digite aqui o valor para converter para segundos: ")) )  

HorasInt = sum(Horas)

Segundos = HorasInt * 3600

print(Segundos)