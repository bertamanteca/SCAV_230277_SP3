def main():
    print("¿Qué quieres ejecutar?")
    print("1. Conversion de resolucion")
    print("2. Conversion de formato ")
    print("3. Comparación de pantalla dividida")
    print("4. GUI")


    ejercicio_elegido = input("Introduce el número: ")

    if ejercicio_elegido == '1':
        import Ex1
        Ex1.ejecutar()
    elif ejercicio_elegido == '2':
        import Ex11
        Ex11.ejecutar()
    elif ejercicio_elegido == '3':
        import Ex2
        Ex2.ejecutar()
    elif ejercicio_elegido == '4':
        import GUI
        GUI.ejecutar()
    elif ejercicio_elegido == '5':
        import ex5
        ex5.ejecutar()
    elif ejercicio_elegido == '6':
        import ex6
        ex6.ejecutar()
    else:
        print("Número de ejercicio no válido. Introduce un número del 1 al 6.")

if __name__ == "__main__":
    main()
