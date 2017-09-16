#Crie uma estrutura que contenha nome e os cursos que o aluno realizou (coloque pelo menos dois alunos).
#Solicite ao usuário que digite qual o curso que deseja buscar.
#Percorra a lista, encontre os usuários que fizeram o curso digitado e mostre o nome do aluno.

alunos = [{"nome":"Mariana", "cursos":["Python"]}, {"nome":"Joao", "cursos":["Python","Infra Agil"]}]

curso = input("Digite o nome do curso: ")
print ("Os alunos que fizeram o curso: ")
for a in alunos:
  for c in a["cursos"]:
  if curso == c:
  print (a["nome"])
