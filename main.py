resultado = 0

while True:
    operacion = input("Escriba la operacion (o salir): ")
    if operacion == "salir":
        break
    if operacion[:1] in ["+", "-", "*", "/", "%"]:
        operacion = "(" + str(resultado) + ")" + operacion
    try:
        resultado = eval(operacion)
        print(resultado)
    except:
        print("Operacion no valida")
