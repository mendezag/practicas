UsuarioDB = 'agustin'
PasswordDB = '123456'
Saldo = 1000


def ValidarUsuario(u, p):
   if u == UsuarioDB and p == PasswordDB:
     return True
   return False

def login():
  print ('Bienvenido')
  usuario = input('Usuario: ')
  password = input('Password: ')
  return ValidarUsuario(usuario,password)

def retirar(valor):
  if valor > Saldo:
    return False, Saldo
  return True, Saldo - valor

def depositar(valor):
  return True, Saldo + valor

def accion(opcion):
  if opcion == 1:
    valor = int(input('cuanto quieres depositar?: '))
    return depositar(valor)

  if opcion == 2:
    valor = int(input('cuanto quieres retirar?: '))
    return retirar(valor)
  
  return False, Saldo

def ejecutar():
  if not login():
    print('usuario o contraseña invalidos')
    return
  
  print('que deseas hacer?')
  opcion = int(input('1. depositar o 2. retirar: '))

  ok, Saldo = accion(opcion)
  if not ok:
    print('no se realizo la accion, tu saldo actual es saldo: ', Saldo)
  else:
    print('accion realizada correctamente, tu saldo actual es: ', Saldo)
ejecutar()