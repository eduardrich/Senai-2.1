L = [5,7,2,9,4,1,3]

Maximo = max(L)

#Mostra a quantidade de numeros que tem na lista "L"
print("Quantidade de numeros na lista:")
print(len(L))

#Mostra o numero mais alto na lista "L"
print("Numero mais alto na lista:")
print(max(L))

#Mostra o menor numero na lista "L"
print("Menor numero na lista:")
print(min(L))

#Mostra a soma dos numeros na lista "L"
print("Soma dos numeros na lista:")
print(sum(L))
print("")

#Ordena os numeros da lista "L" em crescente 
print("Numeros da lista ordenados em forma crescente")
L.sort(key=int)
print(L)
print("")

#Ordena os numeros da lista "L" em decrescente
print("Numeros da lista ordenados em forma decrescente")
L.sort(key=int, reverse=True)
print(L)