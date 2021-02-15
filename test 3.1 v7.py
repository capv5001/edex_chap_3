hrs = input("Ingrese Horas:")
tasa = input("Ingrese tarifa por Horas:")

h = float(hrs)
t = float(tasa)


if h <= 40:
    print(h * t)
    
else:
    print(40 * 10.50 + (h - 40) * (1.5 * t))
