dict = {}
list = []

while True:
    alimento = input('Introduzca el nombre del alimento:')
    cantidad = int(input('Introduzca la cantidad que ha consumido (gramos):'))
    pregunta = input('¿Quiere registrar otro alimento? (Sí/No):')
    
    dict[alimento] = cantidad
    
    if pregunta == 'No':

        print('Resumen del consumo diario: \n')
        print(dict.items())
        break