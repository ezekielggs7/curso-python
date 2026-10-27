
import math
import tkinter as tk
from tkinter import ttk


# Cada función recibe números y devuelve el resultado de una operación.
def sumar(valor1=0, valor2=0):
    return valor1 + valor2


def restar(valor1=0, valor2=0):
    return valor1 - valor2


def multiplicar(valor1=0, valor2=0):
    return valor1 * valor2


def dividir(valor1, valor2):
    # Se evita la división por cero y se informa del problema a la interfaz.
    if valor2 == 0:
        raise ValueError("No se puede dividir entre cero.")
    return valor1 / valor2


def potencia(valor1, valor2):
    return valor1 ** valor2


def raiz_cuadrada(valor):
    # Los números negativos no tienen raíz cuadrada dentro de los números reales.
    if valor < 0:
        raise ValueError("No se puede calcular la raíz cuadrada de un número negativo.")
    return math.sqrt(valor)


# Ventana y controles de la calculadora gráfica.
class CalculadoraApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")
        self.root.resizable(False, False)

        # Contenedor principal donde se organizan los controles.
        frame = ttk.Frame(root, padding=20)
        frame.grid()

        # Etiquetas y campos para escribir los números de la operación.
        ttk.Label(frame, text="Calculadora", font=("Segoe UI", 18, "bold")).grid(
            row=0, column=0, columnspan=2, pady=(0, 16)
        )
        ttk.Label(frame, text="Primer número").grid(
            row=1, column=0, columnspan=2, sticky="w"
        )
        self.valor1 = ttk.Entry(frame, width=30)
        self.valor1.grid(row=2, column=0, columnspan=2, sticky="ew", pady=(4, 12))

        ttk.Label(frame, text="Segundo número (no aplica para raíz)").grid(
            row=3, column=0, columnspan=2, sticky="w"
        )
        self.valor2 = ttk.Entry(frame, width=30)
        self.valor2.grid(row=4, column=0, columnspan=2, sticky="ew", pady=(4, 16))

        # Cada botón guarda su función y si necesita uno o dos números.
        botones = (
            ("Sumar", sumar, True),
            ("Restar", restar, True),
            ("Multiplicar", multiplicar, True),
            ("Dividir", dividir, True),
            ("Potencia", potencia, True),
            ("Raíz cuadrada", raiz_cuadrada, False),
        )
        for indice, (texto, operacion, usa_dos_valores) in enumerate(botones):
            ttk.Button(
                frame,
                text=texto,
                # Los valores predeterminados conservan la operación de este botón.
                command=lambda op=operacion, dos=usa_dos_valores: self.calcular(op, dos),
            ).grid(
                row=5 + indice // 2,
                column=indice % 2,
                sticky="ew",
                padx=4,
                pady=4,
            )

        # Este texto muestra el resultado o un mensaje de error.
        self.resultado = tk.StringVar(value="Ingresa los valores y elige una operación.")
        ttk.Label(
            frame,
            textvariable=self.resultado,
            wraplength=300,
            justify="left",
        ).grid(row=8, column=0, columnspan=2, sticky="w", pady=(14, 10))

        # Acciones para reiniciar los campos o cerrar la ventana.
        ttk.Button(frame, text="Limpiar", command=self.limpiar).grid(
            row=9, column=0, sticky="ew", padx=4
        )
        ttk.Button(frame, text="Salir", command=self.root.destroy).grid(
            row=9, column=1, sticky="ew", padx=4
        )

        self.valor1.focus_set()

    @staticmethod
    def leer_numero(campo):
        # Quita espacios y acepta coma o punto como separador decimal.
        return float(campo.get().strip().replace(",", "."))

    def calcular(self, operacion, usa_dos_valores):
        try:
            valor1 = self.leer_numero(self.valor1)
            # La raíz cuadrada usa solo el primer campo; las demás usan ambos.
            if usa_dos_valores:
                resultado = operacion(valor1, self.leer_numero(self.valor2))
            else:
                resultado = operacion(valor1)
            self.resultado.set(f"Resultado: {resultado}")
        except ValueError as error:
            # Muestra errores de entrada numérica y errores de las operaciones.
            mensaje = str(error) or "Ingresa valores numéricos válidos."
            self.resultado.set(f"Error: {mensaje}")
        except OverflowError:
            self.resultado.set("Error: el resultado es demasiado grande.")

    def limpiar(self):
        # Vacía los campos y deja lista la calculadora para otra operación.
        self.valor1.delete(0, tk.END)
        self.valor2.delete(0, tk.END)
        self.resultado.set("Ingresa los valores y elige una operación.")
        self.valor1.focus_set()


def main():
    # Crea la ventana, coloca la calculadora y espera acciones del usuario.
    root = tk.Tk()
    CalculadoraApp(root)
    root.mainloop()


# Ejecuta la interfaz solo cuando este archivo se inicia directamente.
if __name__ == "__main__":
    main()
