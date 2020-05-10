print('Bienvenido al sistema de solicitud de prestamos bancarios')
print('Por favor a continuacion complete sus datos')
print('Los requisitos para acceder al prestamos son: tener entre 18 y 70 años de edad, \ntener al menos $25.000 como ingresos mensuales')


Nombre = input('Ingrese su nombre de usuario: ')
Apellido = input('Ingrese su apellido: ')
Edad = int(input('Ingrese su edad: '))
Dni = int(input('Ingrese su DNI: '))
IngresoMens = int(input('Ingrese la cantidad de dinero que persive por mes: '))
Email = input('Ingrese su email: ')


def Comprobar():
	if Edad >= 18 and Edad <70 and IngresoMens >= 25000:
		return 'Usted cumple con los requisitos para acceder al prestamo bancario'
	else:
		return 'Lo sentimos mucho, usted no cumple con los requisitos para acceder al prestamo'
print(Comprobar())

print('Muchas gracias por confiar en nuestro sistema')