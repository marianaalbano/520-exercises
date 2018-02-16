#!/usr/bin/python3
# -*- coding: utf-8 -*-
# crie uma classe chamada funcionario com os seguintes atributos:
# nome, salario, idade, area
# crie um metodo para fazer um funcionário ser promovido
#
# crie uma subclasse chamada gerente (ela deve herdar funcionario), com os seguintes atributos:
# quantidade de pessoas na equipe, projeto, objetivo, data do inicio do projeto, prazo para conclusao
# crie um metodo para contratar um novo funcionario (ele pode ter ate 5 funcionarios na equipe)
# crie um metodo para alterar o projeto (não pode ser alterado, caso já esteja em um projeto)
#
# crie uma subclasse chamada programador (ela deve herdar funcionario), com os seguintes atributos:
# gerente, quantidade de linguagem que o analista sabe programar
# crie um metodo para adicionar uma linguagem
# crie um metodo para alterar de qual equipe faz parte (altera o nome do gerente)


class Funcionario():
   
    salario = None
    nome = None
    idade = None
    area = None

    def promover_funcionario(self, salario, area):
        self.salario += salario
        self.area = area
        return ('Parabens %s! Você foi promovido para %s e agora ganha %s ' %(self.nome, self.area, self.salario))


class Gerente(Funcionario):
    equipe = 0
    projeto = None
    objetivo = None
    inicio = None
    fim = None

    def contratar_funcionario(self,quantidade):
        if self.equipe <= 5:
            self.equipe += quantidade
            return ('Voce tem um novo funcionario! Agora a aquipe tem %s pessoas' %self.equipe)

    def alterar_projeto(self,**kwargs):
        if self.projeto:
            return ('Já existe um projeto em andamento, detalhes: \n \
                     Nome: %s\n \
                     Objetivo: %s \n \
                     Inicio: %s \n \
                     Fim: %s' %(self.projeto,
                                self.objetivo,
                                self.inicio,
                                self.fim))
        else:
            self.projeto = kwargs['projeto']
            self.objetivo = kwargs['objetivo']
            self.inicio = kwargs['inicio']
            self.fim = kwargs['fim']
            return "O projeto foi adicionado para o gerente com sucesso!"

class Programador(Funcionario):
    gerente = None
    linguagens = 0

    def adiciona_linguagem(self,linguagem):
        self.linguagens += linguagem
        return ('Parabens, agora voce consegue programar em %s linguagens' %self.linguagens)

    def alterar_equipe(self,gerente):
        print (gerente)
        print (type(gerente))
        self.gerente = gerente
        return ('Agora você faz parte da equipe do gerente %s' %self.gerente)




if __name__ == '__main__':
    pass

    # gerente = Gerente()
    # gerente.nome = 'Mariana'
    # gerente.idade = 22
    # gerente.area = 'Gerente'
    # gerente.salario = 1500
    # print(gerente.promover_funcionario(1500, 'Coordenacao'))
    # print(gerente.alterar_projeto(projeto='teste',objetivo='testar',inicio='10/10/2018',fim='10/12/2018'))
    # print(gerente.alterar_projeto(projeto='teste',objetivo='testar',inicio='10/10/2018',fim='10/12/2018'))
    
    
    
    # programador = Programador()
    # programador.nome = 'Mariana'
    # programador.idade = 22
    # programador.area = 'Programador'
    # programador.salario = 500
    # print(programador.promover_funcionario(400,'Programador Pleno'))
    # print(programador.adiciona_linguagem(1))
    # print(programador.alterar_equipe('Frederico'))