#!/usr/bin/python3

class Vendas:
    def __init__(self):
        self.lista = []

    def cadastro(self, id, nome, quantidade):
        try:
            produto = {'id':id, 'nome':nome,'quantidade':quantidade}
            self.lista.append(produto)
            print ('O produto foi cadastrado com sucesso! \n \n')
        except Exception as e:
            print ('Erro: %s' %e)

    def adicionar(self, id, quantidade):
        try:
            for item in self.lista:
                if id == item['id']:
                    item['quantidade'] += quantidade
                    print ('Estoque atualizado com sucesso')
                    print ('Novo estoque: %s' %item['quantidade'])
                else:
                    raise ValueError('ID da fruta nao encontrado')
        except ValueError as e:
            print ('Erro: %s' %e)
        except Exception as e:
            print ('Erro: %s' %e)

    def vender(self, id, quantidade):
        try:
            for item in self.lista:
                if id == item['id']:
                    item['quantidade'] -= quantidade
                    print ('Item vendido com sucesso')
                    print ('Novo estoque: %s' %item['quantidade'])
                else:
                    raise ValueError('ID da fruta nao encontrado')
        except ValueError as e:
            print ('Erro: %s' %e)
        except Exception as e:
            print ('Erro: %s' %e)
