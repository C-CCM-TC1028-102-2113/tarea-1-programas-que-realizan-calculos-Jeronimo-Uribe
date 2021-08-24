def main():
    #escribe tu código abajo de esta línea
    #Leer los datos
    men=int(input('Dame el número de mensajes: '))
    meg=float(input('Dame el número de megas: '))
    min=int(input('Dame el número de minutos: '))
    cm=(0.80*men)+(0.80*meg)+(0.80*min)
    print('El costo mensual es: %0.2f ' %cm)
    pass


if __name__ == '__main__':
    main()
