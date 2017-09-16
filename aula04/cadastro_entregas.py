#Crie um script para cadastrar entregas, ele deverá solicitar nome e sobrenome.
#Verifique se os dados são do tipo string e grave isto em um nome.txt com o padrão: nome.sobrenome
#Solicite qual é o número do cadastro
#Verifique se o dado é do tipo int e grave isso em um numero.txt
#Caso eu digite 'q' nas duas perguntas ele deve encerrar o programa
#Se a entrega for cadastrada com sucesso, posso cadastrar outra sem iniciar o script novamente



#!/usr/bin/python3
while True:

	print ("Digite abaixo ou pressione '\q' para sair")
	dest = input("Digite o nome do destinatário: ")
	sobrenome = input("Digite o sobrenome do destinatário: ")
	if dest == 'q' or sobrenome == 'q':
		print ("Saindo do programa")
		break

	elif type(dest) == str:
		with open('nomes.txt','a') as f:
		f.write("Remetente: %s.%s \n" %(str.lower(dest), str.lower(sobrenome)))
		print ("Remetente cadastrado \n")

		numero = int(input("Digite o número da entrega: "))
		if type(numero) == int:
			with open ('num_entrega.txt', 'a') as f:
			f.write("Numero da entrega: %s"%(numero))
			print ("Número da entrega cadastrado")
			print ("Entrega cadastrada com sucesso\n \n")
