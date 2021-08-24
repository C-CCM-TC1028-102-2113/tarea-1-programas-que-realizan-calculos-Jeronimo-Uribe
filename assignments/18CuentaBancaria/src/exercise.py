def main():
    #escribe tu código abajo de esta línea
    sma=float(input('Dame el saldo del mes anterior: '))
    i=float(input('Dame los ingresos: '))
    e=float(input('Dame los egresos: '))
    c=float(input('Dame el número de cheques: '))
    t1=sma+i-e
    t2=t1-(c*13)
    t3=t2-(t2*0.075)
    print('El saldo final de la cuenta es: %f' %t3)
    
    pass

if __name__ == '__main__':
    main()
