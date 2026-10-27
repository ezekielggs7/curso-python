# print() muestra texto o valores en la consola.
print("Hello, World!") 


# Una variable guarda un valor para poder usarlo más adelante.
# Estos ejemplos muestran cuatro tipos de datos básicos de Python:
nombre = "Carlos"          # str
edad = 28                  # int
altura = 1.75              # float
es_estudiante = False      # bool

# Una lista guarda varios valores en orden y puede modificarse.
frutas = ["manzana", "banana", "cereza"]
frutas.append("naranja")   # append() agrega un nuevo elemento al final.

# Un diccionario asocia cada clave con un valor.
# Aquí se reutilizan variables anteriores para completar los datos del usuario.
usuario = {
    "nombre": nombre,
    "edad": edad,
    "activo": True
}

# len() cuenta los elementos de la lista y las llaves { } insertan valores
# de variables dentro de una cadena con formato.
print(f"El usuario {usuario['nombre']} tiene {len(frutas)} frutas.")
# type() devuelve el tipo de dato almacenado en una variable.
print(f"El tipo de la variable 'altura' es: {type(altura)}")


def calcular_precio_total(precio_base, impuesto=0.16):
    """Devuelve el precio con impuesto; usa 16 % si no se indica otro."""
    # Calcula el impuesto sobre el precio base y lo suma al precio original.
    iva = precio_base * impuesto
    precio_final = precio_base + iva
    # return entrega el resultado a quien llamó a esta función.
    return precio_final

# Llama a la función con el impuesto predeterminado (0.16, es decir, 16 %).
total_1 = calcular_precio_total(100)
print(f"Total 1: ${total_1}") # Resultado: 116.0

# Este ejemplo reemplaza el impuesto predeterminado por uno de 21 %.
total_2 = calcular_precio_total(100, impuesto=0.21)
print(f"Total 2: ${total_2}") # Resultado: 121.0

# *numeros permite pasar cualquier cantidad de valores posicionales;
# Python los reúne en una tupla dentro de la función.
def sumar_todos(*numeros):
    # sum() suma los valores recibidos y devuelve el total.
    total = sum(numeros)
    return total

# La misma función acepta distintas cantidades de números.
print("Suma de 3 números:", sumar_todos(10, 20, 30))
print("Suma de 5 números:", sumar_todos(5, 5, 5, 5, 5))


# **detalles permite pasar cualquier cantidad de argumentos con nombre;
# Python los reúne en un diccionario.
def registrar_perfil(**detalles):
    # Muestra un título y luego recorre cada par clave-valor del diccionario.
    print("\n--- Registro de Usuario ---")
    for clave, valor in detalles.items():
        # capitalize() pone en mayúscula la primera letra de la clave.
        print(f"{clave.capitalize()}: {valor}")

# Los nombres de los argumentos se convierten en claves y sus valores,
# en los datos que se mostrarán para el perfil.
registrar_perfil(usuario="dev123", rol="Admin", pais="México")
