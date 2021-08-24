def main():
    #escribe tu código abajo de esta línea
    jn=int(input('Dame la cantidad de juegos nuevos: '))
    ju=int(input('Dame la cantidad de juegos usados: '))
    t=(1000*jn)+(350*ju)
    print('El total de la compra es: %0.0f' %t)
   pass



if __name__ == '__main__':
    main()
