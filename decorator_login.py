#exemplo de decorator

# def recebe_funcao(nome_funcao):
#     print (nome_funcao.__name__)
#     def monta_mensagem(retorno_funcao):
#         print (retorno_funcao)
#         mensagem = "Seja bem vindo "+retorno_funcao+"!"
#         return mensagem

#     return monta_mensagem



# @recebe_funcao
# def funcao(nome):
#     return nome


# print (funcao("Mariana"))




#exemplo de decorator para o login

import sys

usuarios = []
login = False

def recebe_funcao(nome):
    def acesso():
        global login
        if login:
            return
        else:
            print ("Você não tem acesso ao sistema")
            return sys.exit()
    return acesso


def acessar_sistema(nome, senha):
    global login
    for user in usuarios:
        if nome == user["nome"] and senha == user["senha"]:
            login = True
            return "Seja bem vindo %s" %nome
    else:
        login = False
        return "Usuário e/ou senha inválidos"

@recebe_funcao
def listar_usuarios():
    return usuarios

@recebe_funcao
def listar_produtos():
    return 'produtos x y z'


def cadastrar_usuario():
    nome = input("Digite o login do novo usuario: ")
    senha = input("Digite o login e senha do nome usuario: ")
    user = {"nome":nome,"senha":senha}
    usuarios.append(user)
    return "Usuario cadastrado com sucesso!"


def menu(opcao):
    if opcao == 1:
        print(cadastrar_usuario())
    elif opcao == 2:
        nome = input('Digite o login: ')
        senha = input('Digite a senha: ')
        print(acessar_sistema(nome, senha))
    elif opcao == 3:
        print (listar_produtos())
    elif opcao == 4:
        print (listar_usuarios())

if __name__ == "__main__":
    while True:
        opcao = int(input("Digite a opcao: "))
        menu(opcao)
