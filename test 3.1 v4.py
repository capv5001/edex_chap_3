hrs = input("Ingrese Horas:")
h = float(hrs)
saln = input("Ingresa salario:")
s = float (saln)

if h <= 40:
    pago = h * s
    print(pago)

else:
    pagon = 40.0 * 10.5
    he = h - 40.0
    pagoe = he * (10.5 * 1.5)
    pago = pagon + pagoe
    print(pago)
