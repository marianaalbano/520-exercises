# O usuário deve digitar o nome do remetente, do destinatário, o produto e a previsão de entrega, isto deve ser gravado em um arquivo.txt

#!/usr/bin/python3

dest = input("Digite o nome do destinatário: ")
remet = input("Digite o nome do remetente: ")
endereco = input("Digite o endereco de entrega: ")
data = input("Digite a previsão de entrega: ")

with open('cadastro.txt','a') as f:
    f.write("\nRemetente: %s - Destinatário: %s - Endereço: %s - Previsão de Entrega: %s" %(dest, remet, endereco, data))

# Após cadastrar algumas entregas, mostre na tela a terceira entrega cadastrada.
with open('cadastro.txt','r') as f:
    entrega = f.readlines()
    print (entrega[5])
