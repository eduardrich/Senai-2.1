#Definição da lista
Val = []

#Pede para inserir os 20 numeros para a media
for c in range(0,20):
    Val.append ( int(input("Digite aqui os valores para a média: ")) )

#detalhamento da soma e conta dos numeros dentro da lista
SomVal = sum(Val)
NumVal = len(Val)

#Tira a media 
MedVal = SomVal / NumVal
print("Media da lista: ")
print(MedVal)

#Numero Max dentro da lista
MaxVal = max(Val)
print("Numero Max da lista:")
print(MaxVal)

#Numero Min dentro da lista
MinVal = min(Val)
print("Numero Min da lista")
print(MinVal)
