string = str(input("Digite uma string qualquer: "))

lista = []

for i in range(1, len(string)+1):
    lista.append(string[-i])

print(lista)
