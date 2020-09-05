# hrs = input("Ingrese Horas:")
# h = float(hrs)

# En esta seccion se comienza por pedir el numero de horas laboradas
hrs = input("escribe las horas laboradas: ")
# Se pasa a convertir la variable a flotante
h = float(hrs)

# En esta seccion se comienza por pedir el salario
salarionormal = input("escriba el salario normal: ")
# Se pasa a convertir la variable a flotante
pagonorm = float(salarionormal)

# Comienza la seccion if, se compara el numero de horas
if h <= 40:
    # Si es VERDADERO (jornada menor o igual a 40 horas)
    # se pasa a realizar la multiplicacion de las horas por salario
    salarioganado = h * pagonorm
    # Se imprime el total
    print(salarioganado)

else:
    # Si es FALSO (jornada mayor a 40 horas) se pasa a
    # la obtencion de una paga normal de 40 hrs
    salarionorm = 40.0 * 10.5
    # Se obtiene el total de horas extra al realiza la diferencia
    # del total de horas menos la jornada normal (40 hrs)
    jornadaextra = h - 40.0
    # Se obtiene el salario extra con el producto de las horas extras
    # por el producto del salario normal por el factor de 150%
    salarioextra = jornadaextra * (10.5 * 1.5)
    # Se obtiene el salario total con la suma del
    # salario de 40 horas mas el salario extra
    salariototal = salarionorm + salarioextra
    # Se imprime el total
    print(salariototal)
