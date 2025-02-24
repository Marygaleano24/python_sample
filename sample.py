def ingresar_puntuacion_comentario():
    while True:
        print('Ingrese una puntuación del 1 al 5:')
        point = input()
        if point.isdecimal():
            point = int(point)
            if 1 <= point <= 5:
                print('Ingrese un comentario:')
                comment = input()
                post = f'Puntuación: {point} Comentario: {comment}'
                with open("data.txt", 'a') as file_pc:
                    file_pc.write(f'{post}\n')
                break
            else:
                print('Ingrese un valor entre 1 y 5.')
        else:
            print('Ingrese un valor numérico para la puntuación.')

def revisar_resultados():
    print('Resultados hasta ahora:')
    try:
        with open("data.txt", "r") as read_file:
            resultados = read_file.read()
            if resultados:
                print(resultados)
            else:
                print('No hay resultados aún.')
    except FileNotFoundError:
        print('No hay resultados aún.')

def main():
    while True:
        print('Seleccione la operación que desea realizar:')
        print('1: Ingresar puntuación y comentario')
        print('2: Revisar resultados')
        print('3: Salir')
        num = input()

        if num.isdecimal():
            num = int(num)
            if num == 1:
                ingresar_puntuacion_comentario()
            elif num == 2:
                revisar_resultados()
            elif num == 3:
                print('Saliendo...')
                break
            else:
                print('Ingrese un valor entre 1 y 3.')
        else:
            print('Ingrese un valor entre 1 y 3.')

if __name__ == "__main__":
    main()
