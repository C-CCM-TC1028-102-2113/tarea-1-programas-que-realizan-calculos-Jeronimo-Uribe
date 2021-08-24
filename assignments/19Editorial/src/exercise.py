def main():
    #escribe tu código abajo de esta línea
    npal=int(input('Dame el número de palabras: '))
    npag=math.ceil(npal/475)
    c1=npag*60
    c2=c1-(c1*.1)
    print('El costo de la publicación es: %f' %c2)
    pass


if __name__ == '__main__':
    main()
