import random


# Cada dificultad define el número máximo posible y los intentos permitidos.
DIFICULTADES = {
    "1": ("Fácil", 50, 10),
    "2": ("Normal", 100, 7),
    "3": ("Difícil", 100, 5),
}


def elegir_dificultad():
    """Pide una dificultad y devuelve sus límites, o None para salir."""
    while True:
        print("\nElige una dificultad:")
        print("1. Fácil: número del 1 al 50, con 10 intentos")
        print("2. Normal: número del 1 al 100, con 7 intentos")
        print("3. Difícil: número del 1 al 100, con 5 intentos")
        print("S. Salir")

        # Acepta la letra de salida y evita distinguir entre mayúsculas y minúsculas.
        opcion = input("Tu opción: ").strip().lower()
        if opcion == "s":
            return None
        if opcion in DIFICULTADES:
            return DIFICULTADES[opcion]

        # Si no coincide con las opciones disponibles, se vuelve a mostrar el menú.
        print("Opción no válida. Elige 1, 2, 3 o S.")


def jugar_ronda(nombre_dificultad, maximo, limite_intentos):
    """Juega una partida y devuelve los intentos usados si se gana."""
    # randint incluye ambos extremos, así que el secreto puede ser 1 o maximo.
    numero_secreto = random.randint(1, maximo)
    intentos = 0
    pista_disponible = True

    print(
        f"\nDificultad {nombre_dificultad}: adivina el número "
        f"entre 1 y {maximo}."
    )
    print(
        f"Tienes {limite_intentos} intentos. "
        "Escribe 'pista' para conocer si el número es par o impar."
    )
    print("Escribe 'salir' si quieres abandonar esta partida.")

    # La ronda continúa mientras queden intentos y no se haya acertado.
    while intentos < limite_intentos:
        entrada = input(
            f"\nIntento {intentos + 1}/{limite_intentos}: "
        ).strip().lower()

        # Permite terminar la ronda sin cerrar todo el programa.
        if entrada == "salir":
            print(f"Partida cancelada. El número era {numero_secreto}.")
            return None

        # La pista se puede pedir una sola vez y no consume un intento.
        if entrada == "pista":
            if pista_disponible:
                paridad = "par" if numero_secreto % 2 == 0 else "impar"
                print(f"Pista: el número secreto es {paridad}.")
                pista_disponible = False
            else:
                print("Ya utilizaste la pista de esta partida.")
            continue

        # Convierte la respuesta a entero; texto no numérico no cuenta como intento.
        try:
            adivinanza = int(entrada)
        except ValueError:
            print("Escribe un número entero, 'pista' o 'salir'.")
            continue

        # Solo las respuestas dentro del rango cuentan para el límite de intentos.
        if not 1 <= adivinanza <= maximo:
            print(f"El número debe estar entre 1 y {maximo}; no cuenta como intento.")
            continue

        intentos += 1

        # Da una orientación según la relación entre la respuesta y el secreto.
        if adivinanza < numero_secreto:
            print("Demasiado bajo. Prueba con un número mayor.")
        elif adivinanza > numero_secreto:
            print("Demasiado alto. Prueba con un número menor.")
        else:
            print(f"¡Correcto! Adivinaste en {intentos} intentos.")
            return intentos

    # Si el ciclo termina sin acertar, se agotó el límite de intentos.
    print(f"Se acabaron los intentos. El número secreto era {numero_secreto}.")
    return None


def main():
    """Muestra el menú, administra las partidas y guarda estadísticas."""
    print("¡Bienvenido al juego de adivinar el número!")

    # Estas estadísticas se conservan mientras el programa siga abierto.
    partidas_ganadas = 0
    mejor_puntuacion = None

    # El menú de dificultad se repite para permitir jugar varias partidas.
    while True:
        dificultad = elegir_dificultad()
        if dificultad is None:
            break

        nombre, maximo, limite_intentos = dificultad
        resultado = jugar_ronda(nombre, maximo, limite_intentos)

        # Solo una ronda ganada devuelve un número de intentos.
        if resultado is not None:
            partidas_ganadas += 1
            if mejor_puntuacion is None or resultado < mejor_puntuacion:
                mejor_puntuacion = resultado
                print("¡Nuevo récord de esta sesión!")

        # Presenta el resumen de victorias y el mejor resultado conseguido.
        print(f"Partidas ganadas: {partidas_ganadas}")
        if mejor_puntuacion is not None:
            print(f"Mejor resultado: {mejor_puntuacion} intentos.")

        # Permite iniciar otra partida o regresar al menú de salida.
        while True:
            volver_a_jugar = input("¿Quieres jugar otra vez? (s/n): ").strip().lower()
            if volver_a_jugar in ("s", "si", "sí"):
                break
            if volver_a_jugar in ("n", "no"):
                print("¡Gracias por jugar!")
                return
            print("Respuesta no válida. Escribe 's' o 'n'.")

    # Se muestra también al salir desde el menú de dificultad.
    print("¡Gracias por jugar!")


# Ejecuta el juego solo al iniciar este archivo directamente.
if __name__ == "__main__":
    main()
