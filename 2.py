#Definição das listas
PriList = []
SegList = []
TerList = []
QuartList = []
SomaLista = int
DadosLista = int

#Solicitação para inserção do 1 valor
for c in range(0,1):
    PriList.append ( int(input("Digite aqui o 1 valor para a média: ")) )  

#Solicitação para inserção do 2 valor
for c in range(0,1):
    SegList.append ( int(input("Digite aqui o 2 valor para a média: ")) )  

#Solicitação para inserção do 3 valor
for c in range(0,1):
    TerList.append ( int(input("Digite aqui o 3 valor para a média: ")) )  

#Solicitação para inserção do 4 valor
for c in range(0,1):
    QuartList.append ( int(input("Digite aqui o 4 valor para a média: ")) )  

#Soma do valor das listas
SomaLista = PriList + SegList + TerList + QuartList

#Soma da quantia de numeros da lista
DadosLista = len(PriList) + len(SegList) + len(TerList) + len(QuartList)

#Converte a lista "SomaLista" para uma Variavel Int
SomaListaInt = sum(SomaLista)

#Da a Media dos valores
Media = SomaListaInt / DadosLista

print(Media)
