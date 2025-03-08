#US-001/create_register

user = []

def user_register():
  id = int(input("agregue su id"))
  user.append(id)
  name = input("agregue su nombre")
  user.append(name)
  last_name = input("agregue su apellido")
  user.append(last_name)
  email = input("agregue su email")
  user.append(email)
  password = input("cree una contraseña de 8 caracteres entre numeros y letras")
  user.append(password)
  print("usuario creado exitosamente")
  print(user)