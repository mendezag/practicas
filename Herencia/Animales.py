from Seres_vivos import *

#LA CLASE FELINOS HEREDA ALGUNOS ATRIBUTOS DE LA CLASE SERES_VIVOS
class Felinos(Seres_vivos):
	pass

	def descripcion_General(self):
		print("Los felinos esta compuesto de la siguente manera: ")
		print("1- Nombre: ",self.nombre, "\n2- Sexo: ",self.sexo,"\n4- adn: "
		,self.adn,"\n5- esqueleto: ",self.esqueleto,"\n6- venas: "	
		,self.venas,"\n7- musculos: ",self.musculos,"\n8- piel: ",self.piel)

# LA CLASE FELINOS TIENE SUS PROPIOS METODOS O ACCIONES 
	def caza(self):
		self.cazar = True
		print("Puedo cazar")
	def ronroneo(self):
		self.ronronear = True
		print("Puedo ronronear")
	def garras_retractiles(self):
		self.esconder_garras = True
		print("Tengo las garras esocondidas")
		

Leon = Felinos("Leon","Macho")
Leon.descripcion_General()
print("=====CARACTERISTICAS DE LOS FELINOS======")
Leon.caza()
Leon.ronroneo()
Leon.garras_retractiles()