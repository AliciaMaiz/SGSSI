from collections import Counter
def aplicar_sustituciones(mensaje_original, sustituciones):
    resultado = ""
    for c in mensaje_original:
        if c.upper() in sustituciones:
            letra_sust = sustituciones[c.upper()]
            resultado += letra_sust if c.isupper() else letra_sust.lower()
        else:
            resultado += c
    return resultado
def contarLetras(mensaje):
  mensaje = mensaje.replace(" ", "").upper()
  conteo = Counter(mensaje)
  conteo = {k: v for k, v in conteo.items() if k.isalpha()}
  letras_ordenadas = sorted(conteo.items(), key=lambda item: item[1], reverse=True)
  print(letras_ordenadas)

def mostrar_tabla(sustituciones):
    print("\nTabla de sustituciones:")
    for c in sorted(sustituciones):
        print(f"{c} → {sustituciones[c]}")
    print()

def obtener_letras_sin_sustituir(mensaje, sustituciones):
    letras = set(c.upper() for c in mensaje if c.isalpha())
    sin_sustituir = sorted(letras - set(sustituciones.keys()))
    return sin_sustituir

def main():
    mensaje = input("Introduce el mensaje cifrado:\n")
    contarLetras(mensaje)
    sustituciones = {}

    while True:
        descifrado = aplicar_sustituciones(mensaje, sustituciones)
        print("\nMensaje descifrado actual:")
        print(descifrado)

        mostrar_tabla(sustituciones)

        sin_sustituir = obtener_letras_sin_sustituir(mensaje, sustituciones)
        if sin_sustituir:
            print("Letras sin sustituir:", " ".join(sin_sustituir))
        else:
            print(" Todas las letras han sido sustituidas.")

        opc = input("\n¿Quieres hacer una sustitución manual? (y/n): ").lower()
        if opc != "y":
            break

        original = input("Letra cifrada a cambiar: ").upper()
        if original not in sin_sustituir:
            print(" Esa letra ya ha sido sustituida o no está en el mensaje.")
            continue

        nueva = input("Letra a mostrar en su lugar: ").upper()
        if len(nueva) != 1 or not nueva.isalpha():
            print(" Letra inválida.")
            continue

        if nueva in sustituciones.values():
            print(f"La letra '{nueva}' ya está siendo usada como sustitución.")
            confirmar = input("¿Estás seguro que quieres usarla de nuevo? (y/n): ").lower()
            if confirmar != 'y':
                continue

        sustituciones[original] = nueva

    print("\n Mensaje final descifrado:")
    print(aplicar_sustituciones(mensaje, sustituciones))
    mostrar_tabla(sustituciones)

if __name__ == "__main__":
    main()
