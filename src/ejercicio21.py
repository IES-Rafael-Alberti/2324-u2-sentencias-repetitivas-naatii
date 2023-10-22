def procesarMonto(monto:int)->int:
    descuento = 0.1
    if monto > 1000:
        return round(monto*descuento,2)
    else:
        return monto

if __name__=="__main__":
    try:
        monto = 1
        montoTotal = 0
        while monto != 0:
            monto = procesarMonto(int(input("Ingrese un monto: ")))
            if monto > 0:
                montoTotal += monto
        print(montoTotal)
    except ValueError:
        raise ValueError()