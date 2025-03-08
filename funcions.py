user = []
def user_register():
    id = int(input("Agregue su id"))
    user.append(id)
    name = input("Agregue su nombre")
    user.append(name)
    las_name = input("Agrega tu apellido")
    user.append(las_name)
    password = input("Cree su password de 8 caracteres")
    user.append(password)
    print("Usuario creado exitosamente")
    print(user)