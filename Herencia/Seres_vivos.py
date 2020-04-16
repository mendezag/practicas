class Seres_vivos():
	#ATRIBUTOS INICIALES DE UN SER VIVO
	def __init__(self,nombre, sexo):
		self.nombre = nombre
		self.sexo = sexo
		self.espiritu = True
		self.adn = True
		self.esqueleto = True
		self.venas = True
		self.musculos = True
		self.piel = True
#METODOS O ACCIONES QUE SON CAPACES DE HACER LOS HUMANOS
	def respirar(self):
		respirando = True
		print("esta respirando")
	def caminar(self):
		caminando = False
		print("esta caminando")
	def hablar(self):
		habla = False
		print("esta hablando")

	def descripcion_General(self):
		print("ADAN esta compuesto de la siguente manera: ")
		print("1- Nombre: ",self.nombre, "\n2- Sexo: ",self.sexo, "\n3- espiritu: ",self.espiritu,"\n4- adn: "
		,self.adn,"\n5- esqueleto: ",self.esqueleto,"\n6- venas: "	
		,self.venas,"\n7- musculos: ",self.musculos,"\n8- piel: ",self.piel)

#LA CLASE EVA HEREDA LOS METODOS DE LA CLASE SERES_HUMANOS
class Eva(Seres_vivos):
	pass
	def descripcion_General(self):
		print("EVA esta compuesto de la siguente manera: ")
		print("1- Nombre: ",self.nombre, "\n2- Sexo: ",self.sexo, "\n3- espiritu: ",self.espiritu,"\n4- adn: "
		,self.adn,"\n5- esqueleto: ",self.esqueleto,"\n6- venas: "	
		,self.venas,"\n7- musculos: ",self.musculos,"\n8- piel: ",self.piel)

#OBJETO NUMERO UNO DE MI CLASE SERES_HUMANOS
print("========ADAN============")
Adan = Seres_vivos("Adan","Hombre")
Adan. descripcion_General()
print("=========================")
Adan.respirar()
Adan.caminar()
Adan.hablar()
#CLASE EVA QUE HEREDA DE LA CLASE SERES_HUMANOS
print("=======EVA=============")
Eva = Eva("Eva","Mujer")
Eva.descripcion_General()
print("=====================")
Eva.respirar()
Eva.caminar()
Eva.hablar()