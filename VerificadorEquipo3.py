Equipo = "Lechugas" 
integrantes = ["Raymundo", "Alberto", "Sebastian", "Jared", "Brenda"]

print("El equipo es:", Equipo)
print("Los integrantes del equipo son:")
for integrante in integrantes:
    print("-", integrante)

contraseñas = ["Uva2", "Komala1970", "Fulljosh", "Palpit0ad", "Gwenely17", "Desklewis", "parissesw", "Lolo", "Tulio31", "Leche"] 

def verificar(contraseñas):
    for contrasena in contraseñas:
        if len(contrasena) < 6:
            return "Débil"
        elif len(contrasena) >= 6 and not any(c.isdigit() for c in contrasena):
            return "Media"
        else:
            return "Fuerte"

print("\nResultados de la verificación de contraseñas:")        
for contrasena in contraseñas:
    resultado = verificar([contrasena])
    print(f"La contraseña '{contrasena}' es: {resultado}")
