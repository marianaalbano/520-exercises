# Criar dois arquivos diferentes, no primeiro arquivo deve conter:
# Uma classe menu com as seguintes opcoes: 1 cadastrar fruta, 2 adicionar fruta ao estoque, 3 vender fruta
# O segundo arquivo deve conter:
# Uma classe de Vendas com as opções correspondente ao menu

from Menu import Menu


def chamar_menu():
    menu = Menu()
    while True:
        menu.opcao()


if __name__ == '__main__':
    chamar_menu()
