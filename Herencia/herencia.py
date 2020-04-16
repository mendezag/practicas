
print("En este programa vamos a simular la funcionalidad basica de un vehiculo")

#Definimos las caracteristicas basicas del automovil
class Vehiculo():
	def __init__(self,marca, modelo):
		self.marca = marca
		self.modelo = modelo
		self.ruedas = 4
		self.asientos = 5
		self.encendido = False

#Definimos las funcionalidades que tiene nuestro vehiculo
	print("CARACTETISTICAS DEL COCHE")	

	def caracteristicas(self):
		print("La marca de mi coche es: ",self.marca, "\nEl modelo de mi coche es: ",self.modelo,
		 "\nEl numero de ruedas es de: ",self.ruedas, "\nLa cantidad de asientos es de: ",self.asientos,
		 "\nEl coche se encuentra encendido: ", self.encendido)

#FUNCION PARA DAR ARRANQUE A NUESTRO COCHE
	
	def arrancar(self):
		self.encendido = True 
		print("HEMOS ARRANCADO EL COCHE ") 
		print("La marca de mi coche es: ",self.marca, "\nEl modelo de mi coche es: ",self.modelo,
		 "\nEl numero de ruedas es de: ",self.ruedas, "\nLa cantidad de asientos es de: ",self.asientos,
		 "\nEl coche se encuentra encendido: ", self.encendido)

class Moto(Vehiculo):
	def __init__(self,marca, modelo):
		self.marca = marca
		self.modelo = modelo
		self.ruedas = 2
		self.asientos = 2
		self.encendido = False

	def caracteristicas(self):
		print("La marca de mi coche es: ",self.marca, "\nEl modelo de mi coche es: ",self.modelo,
		 "\nEl numero de ruedas es de: ",self.ruedas, "\nLa cantidad de asientos es de: ",self.asientos,
		 "\nEl coche se encuentra encendido: ", self.encendido)

		
#MI OBJETO DE CLASE VEHICULO 
miCoche = Vehiculo("Peugeot", "207")
miCoche.caracteristicas()
#miCoche.arrancar()

print("====================================================================================================")
print("====================================================================================================")
#SEGUDNO OBJETO DE MI CLASE VEHICULO
miMoto = Moto("Honda","CBR")
miMoto.caracteristicas()
miMoto.arrancar()