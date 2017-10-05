#!/usr/bin/python3
from Vendas import Vendas


class Menu():

    def __init__(self):
        print ('aqui')
        self.vendas = Vendas()

    def opcao(self):
        try:
            print ('\n1 - Cadastro \
                    \n2 - Adicionar ao estoque \
                    \n3 - Vender produto\n')
            opcao = int(input('digite uma opcao: '))
            if opcao == 1:
                try:
                    id = int(input('ID:'))
                    nome = input('NOME:')
                    quantidade = int(input('QUANTIDADE:'))
                    self.vendas.cadastro(id, nome, quantidade)
                except ValueError as e:
                    print ('Erro: Id e quantidade devem ser NUMEROS \n \n')
                except Exception as e:
                    print ('Erro: %s' %e)

            elif opcao == 2:
                try:
                    id = int(input('ID:'))
                    quantidade = int(input('QUANTIDADE:'))
                    self.vendas.adicionar(id, quantidade)
                except ValueError as e:
                    print ('Erro: Id e quantidade devem ser NUMEROS \n \n')
                except Exception as e:
                    print ('Erro: %s' %e)

            elif opcao == 3:
                try:
                    id = int(input('ID:'))
                    quantidade = int(input('QUANTIDADE:'))
                    self.vendas.vender(id, quantidade)
                except ValueError as e:
                    print ('Erro: Id e quantidade devem ser NUMEROS \n \n')
                except Exception as e:
                        print ('Erro: %s' %e)
            else:
                print ('Ocorreu um erro')
        except KeyboardInterrupt as e:
            print ('\nsaindo...')
            exit()
        except Exception as e:
            print ('Ocorreu um erro no Menu')
            
