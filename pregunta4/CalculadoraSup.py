def calcuSup(operacion):
    def suma(a,b):
        return a+b
    def multiplicacion(a,b):
        return a*b

        if operacion == "suma":
            return suma
        elif operacion == "multi":
            return multiplicacion

    fGuardada = seleccion("suma")
    

    print fGuardada( 5,6)