CONTRASEÑA = "contraseña"

def adivinarContraseña(contraseñaUsuario:str)->bool:
    return True if contraseñaUsuario == CONTRASEÑA else False

if __name__=="__main__":
    contraseñaUsuario = input("Introduzca una contraseña: ")
    while not adivinarContraseña(contraseñaUsuario): contraseñaUsuario = input("Introduzca una contraseña: ")
    else: print(contraseñaUsuario)