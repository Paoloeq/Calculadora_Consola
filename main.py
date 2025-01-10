# Lo colocaré como función a la calculadora
def Calculadora():
    print("Bienvenido a la calculadora en python :D")

    # Pedimos los números
    num1 = float(input("Ingresa el número 1: "))
    num2 = float(input("Ingrese el número 2: "))
    
    # Elegir la operación
    print("Selecciona la operación: ")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    operacion = input("Ingresa el número de la operación (1/2/3/4)")

    # Calcular el Resultado
    if operacion == "1":
        resultado = num1 + num2
        print(f"El resultado de la operación es : {resultado}")
    elif operacion == "2":
        resultado = num1 - num2
        print(f"El resultado de la operación es: {resultado}")
    elif operacion == "3":
        resultado = num1 * num2
        print(f"El resultado de la operación es: {resultado}")
    elif operacion == "4":
        if num2!=0:
            resultado = num1 / num2
            print(f"El resultado de la operación es: {resultado}")
        else:
            print("no se puede dividir entre cero")
    else: print("Operación no valida intenta de nuevo")

# Llamar a la función
Calculadora()