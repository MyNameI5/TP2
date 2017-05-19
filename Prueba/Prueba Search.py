def aa(contraseña):
    with open(prueba, 'r') as inF:
        for line in inF:
            if contraseña in line:
                print("Contraseña Encontrada")
