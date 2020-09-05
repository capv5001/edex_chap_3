hrs = input("Ingrese Horas:")
saln = input("Ingresa salario:")

h = float(hrs)
s = float(saln)

if h <= 40:
    pago = h * s
    print(pago)

else:
    pagon = 40.0 * 10.5
    he = h - 40.0
    pagoe = he * (10.5 * 1.5)
    pago = pagon + pagoe
    print(pago)
