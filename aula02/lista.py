#!/usr/bin/python3

lista = [{"indice1":1,"indice2":2},"feijão","batata",[5,6,7]]
print("Imprimindo minha lista \n")

# Imprima o conteudo do indice1
print(lista[0]["indice1"])

# Remova o "feijão" da lista
# lista.remove("feijão")
lista.pop(1)
print(lista)

# Inclua o valor inteiro 8 na lista numérica
lista[2].append(8)
print(lista)

# Inclua o valor flutuante do PI (3,14) na lista numérica
lista.append(3.14)
print(lista)

# Inclua um dicionário de produtos de mercado na sua lista principal
dicionario = {"produto1": "bacon", "produto2": "mais bacon", "produto3": "mais bacon ainda"}
lista.append(dicionario)
print(lista)

# Inclua o indice3 no dicionario de indices
lista[0]["indice3"] = 3
print(lista)
