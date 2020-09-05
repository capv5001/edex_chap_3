hrs = input("Ingrese Horas:")
saln = input("Ingresa salario:")

if float(hrs) <= 40:
    pago = float(hrs) * float(saln)
    print(pago)

else:
    pagon = 40.0 * 10.5
    he = float(hrs) - 40.0
    pagoe = he * (10.5 * 1.5)
    pago = pagon + pagoe
    print(pago)
