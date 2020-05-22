class Pokemon():
	def __init__(self,nombre,tipo):
		self.nombre = nombre
		self.tipo = tipo
	
	def Descripcion(self):
		return '{} es de tipo {}'.format(self.nombre,self.tipo)

class pikachu (Pokemon):
	def ataque(self,tipo_ataque):
		return '{} está atacando con {}'.format(self.nombre,tipo_ataque)


class charmander(Pokemon):
	def ataque(self,tipo_ataque):
		return '{} está atacando con {}'.format(self.nombre,tipo_ataque)

class squirtle (Pokemon):
	def ataque(self,tipo_ataque):
		return '{} está atacando con {}'.format(self.nombre,tipo_ataque)

pokemon1 = pikachu('Pikachu','Electrico')
print(pokemon1.Descripcion())
print(pokemon1.ataque('impactrueno'))
print("                      ")
pokemon2 = charmander('Charmander','Fuego')
print(pokemon2.Descripcion())
print(pokemon2.ataque('Bola de Fuego'))
print("                      ")
pokemon3 = squirtle('Squirtle','Agua')
print(pokemon3.Descripcion())
print(pokemon3.ataque('Pistola de Agua'))