def recaudar_datos_persona():
    print("--- Registro de Datos Personales ---")
    
    nombre = input("Ingresa el nombre: ").strip()
    
    # Conversión a entero para la edad
    while True:
        try:
            edad = int(input("Ingresa la edad: "))
            break
        except ValueError:
            print("Por favor, introduce un número válido para la edad.")
            
    correo = input("Ingresa el correo electrónico: ").strip()
    telefono = input("Ingresa el número de teléfono: ").strip()

    # Guardar los datos en un diccionario
    persona = {
        "nombre": nombre,
        "edad": edad,
        "correo": correo,
        "telefono": telefono
    }

    print("\n--- Datos Recopilados ---")
    for clave, valor in persona.items():
        print(f"{clave.capitalize()}: {valor}")

    return persona

# Ejecutar la función
if __name__ == "__main__":
    datos = recaudar_datos_persona()
