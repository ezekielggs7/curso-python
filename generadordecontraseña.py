import argparse
import secrets
import string


def generar_contrasena_segura(longitud: int = 16) -> str:
    """Genera una contraseña con minúsculas, mayúsculas, números y símbolos."""
    # Rechaza valores que no sean enteros y longitudes demasiado cortas.
    if type(longitud) is not int:
        raise ValueError("La longitud debe ser un número entero.")
    if longitud < 8:
        raise ValueError("La longitud mínima para una contraseña segura es de 8 caracteres.")

    # Define los cuatro grupos de caracteres que debe incluir cada contraseña.
    grupos = (
        string.ascii_lowercase,
        string.ascii_uppercase,
        string.digits,
        string.punctuation,
    )
    # Elige primero un carácter aleatorio de cada grupo para asegurar que
    # todos estén representados, usando el generador seguro del módulo secrets.
    caracteres = [secrets.choice(grupo) for grupo in grupos]
    # Combina los grupos para poder completar el resto de la longitud solicitada.
    todos_los_caracteres = "".join(grupos)
    caracteres.extend(
        secrets.choice(todos_los_caracteres) for _ in range(longitud - len(caracteres))
    )
    # Mezcla el orden para que los caracteres obligatorios no queden al principio.
    secrets.SystemRandom().shuffle(caracteres)
    # Une los caracteres individuales y devuelve la contraseña final.
    return "".join(caracteres)


def pedir_entero(mensaje: str, minimo: int, predeterminado: int) -> int:
    # Repite la pregunta hasta que se reciba un entero que cumpla el mínimo.
    while True:
        # strip() elimina espacios; si no se escribe nada, se usa el valor sugerido.
        respuesta = input(f"{mensaje} (predeterminado {predeterminado}): ").strip()
        if not respuesta:
            return predeterminado

        try:
            # Convierte el texto ingresado a un número entero.
            valor = int(respuesta)
        except ValueError:
            # Si la conversión falla, informa al usuario y vuelve a preguntar.
            print("Introduce un número entero.")
            continue

        # No acepta valores menores al mínimo configurado para esa pregunta.
        if valor < minimo:
            print(f"El valor mínimo permitido es {minimo}.")
            continue
        return valor


def main() -> None:
    # Configura el análisis de opciones para poder usar el programa desde la terminal.
    parser = argparse.ArgumentParser(
        description="Genera contraseñas aleatorias usando el generador seguro de Python."
    )
    # -l/--longitud permite indicar cuántos caracteres tendrá cada contraseña.
    parser.add_argument(
        "-l",
        "--longitud",
        type=int,
        default=None,
        help="longitud de cada contraseña (mínimo: 8; predeterminado: 16)",
    )
    # -n/--cantidad permite indicar cuántas contraseñas se generarán.
    parser.add_argument(
        "-n",
        "--cantidad",
        type=int,
        default=None,
        help="número de contraseñas a generar (predeterminado: 1)",
    )
    # Lee las opciones de la línea de comandos, si el usuario proporcionó alguna.
    args = parser.parse_args()

    # Valida las opciones escritas en la terminal y muestra un error de uso
    # si no respetan los límites permitidos.
    if args.longitud is not None and args.longitud < 8:
        parser.error("--longitud debe ser al menos 8.")
    if args.cantidad is not None and args.cantidad < 1:
        parser.error("--cantidad debe ser al menos 1.")

    # Si no se especificó la longitud en la terminal, la solicita de forma interactiva.
    longitud = args.longitud
    if longitud is None:
        longitud = pedir_entero("¿Qué longitud quieres para la contraseña?", 8, 16)

    # Si no se especificó la cantidad, solicita cuántas contraseñas generar.
    cantidad = args.cantidad
    if cantidad is None:
        cantidad = pedir_entero("¿Cuántas contraseñas quieres generar?", 1, 1)

    # Genera la cantidad elegida; range(cantidad) repite el bloque ese número de veces.
    for numero in range(cantidad):
        contrasena = generar_contrasena_segura(longitud)
        if cantidad > 1:
            # Numera los resultados cuando se generan varias contraseñas.
            print(f"{numero + 1}. {contrasena}")
        else:
            # Para un único resultado, muestra primero su longitud y luego la contraseña.
            print(f"Tu contraseña segura ({longitud} caracteres) es:")
            print(contrasena)


# Llama a main() solo al ejecutar este archivo directamente,
# no cuando se importa desde otro módulo.
if __name__ == "__main__":
    main()
