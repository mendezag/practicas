#CREAMOS VARIAS CLASES CON SU METODOS CORRESPONDIENTES
class Personas():

	def Desplazamiento(self):
		print("Me desplazo con mis piernas")

class Animales_terrestres():

	def Desplazamiento(self):
		print("Me dezplazo con mis patitas")

class Animales_acuaticos():

	def Desplazamiento(self):
		print("Me dezplazo con mis aletas")

class Animales_voladores():

	def Desplazamiento(self):
		print("Me dezplazo con mis alas")

#PARA HACER USO DEL POLIMORFISMO CREAMOS UN METODO Y LE PASAMOS UN PARAMETRO
def Desplazamientos(ser_vivo):
	#UTILIZAMOS EL PARAMETRO QUE ASIGNAMOS AL METODO "DESPLAZAMIENTOS" PARA LLAMAR AL METODO DESPLAZAMIENTO
	ser_vivo.Desplazamiento()
#CREAMOS UN OBJETO Y LE ASIGNAMOS UN VALOR PARA DECIRLE DE QUE TIPO ES
ser_viviente = Personas()
#LLAMAMOS AL METODO DESPLAZAMIENTOS Y LE PASAMOS POR PARAMETRO NUESTRO OBJETO Y DE ESTA MANERA VEMOS EL POLIMORFISMO
#YA QUE CUANDO LE ASIGNAMOS A NUESTRO OBJETO EL VALOR DE A QUE TIPO DE CLASE PERTENECE AUTOMATICAMENTE SABE QUE METODO DESPLAZAMIENTO LLAMAR
Desplazamientos(ser_viviente)
#PARA LLAMAR AL METODO DESPLAZAMIENTO DE LAS DEMAS CLASES SOLAMENTE BORREN EL "#" QUE SE ENCUENTRA DELANTE DE LAS SIGUIENTES LINEAS DE CODIDO

#Desplazamientos(ser_viviente)
#ser_viviente = Animales_terrestres()
#Desplazamientos(ser_viviente)
#ser_viviente = Animales_acuaticos()
#Desplazamientos(ser_viviente)
#ser_viviente = Animales_voladores()
#Desplazamientos(ser_viviente)