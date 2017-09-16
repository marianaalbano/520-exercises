# criar uma classe chamada Carro
# ela deve ter os atributos: velocidade máxima e velocidade atual (zero)
# criar um método para acelerar, ele deve verificar a velocidade atual e se for menor que a velocidade máxima, somar a velocidade. Caso contrario mostrar que atingiu o limite de velocidade.
# criar um método para frear, ele deve verificar a velocidade atual, se for maior do que zero, abaixar a velocidade. Se for igual a zero, mostrar que o carro já está parado.

class Carro():
  vel_max = 200
  vel_atual = 0

  def acelerar(self,acel):
  if acel > 200:
                 print ("Voce nao pode acelerar tudo isso")
  elif self.vel_atual < self.vel_max and acel <= self.vel_max:
                 self.vel_atual += acel
                 if self.vel_atual > 200:
                      print ("Voce nao pode acelerar tudo isso")
                 else:
                     print ("Velocidade atual",self.vel_atual)
  else:
                 print ("Voce atingiu o limite de velocidade")

  def frear(self,acel):
             if self.vel_atual > 0:
                 self.vel_atual -= acel
                 print ("Velocidade atual",self.vel_atual)
             else:
                 print ("O carro esta parado")

if __name__ == '__main__':
  car = Carro()
  car.acelerar(50)
  car.acelerar(100)
  car.acelerar(100)
