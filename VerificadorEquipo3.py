Equipo = "Lechugas" 
integrantes = ["Raymundo", "Alberto", "Sebastian", "Jared", "Brenda"]

print("El equipo es:", Equipo)
print("Los integrantes del equipo son:")
for integrante in integrantes:
    print("-", integrante)

def verificar(contrasena):
    if len(contrasena) < 6:
        return "Débil"
    elif len(contrasena) >= 6 and not any(c.isdigit() for c in contrasena):
        return "Media"
    else:
        return "Fuerte"

contraseñas = ["Uva2", "Komala1970", "Fulljosh", "Palpit0ad", "Gwenely17", "Desklewis", "parissesw", "Lolo", "Tulio31", "Leche"] 

print("Lista de contraseñas:")
for i, c in enumerate(contraseñas, 1):
    print(f"{i}. {c}")

for contraseña in contraseñas:
    resultado = verificar(contraseña)
    print("Contraseña:", contraseña, "-", resultado)
