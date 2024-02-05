def OrdenarLista(listaNum):
    """Función que recibe una lista de números enteros y los escribe en
    un fichero llamado 'ListaOrdenada.txt' ordenándolos de mayor a menor
    en el archivo.
    
    Parámetro: listaNum = Lista de numeros enteros.
    Salida: La función no devuelve nada.
    
    """
    listaNum.sort()
    listaNum.reverse()
    with open ('ListaOrdenada.txt', 'w') as file:
        for index in listaNum:
            file.write(str(index))

OrdenarLista([2,7,1,4,9]) #Código ejemplo

def NumeroPar(fichero):
    """Función que abre un fichero que contiene una lista ordenada de números,
    lo lee y escribe en otro fichero, llamado 'Lista De Pares.txt', solo los
    números pares del fichero de entrada.
    
    Parámetro: fichero = fichero que contiene una lista ordenada de números.
    Salida: No devuelve ningún valor.
    
    """
    import os
    if os.path.isfile(fichero):
        with open (fichero,'r') as file:
            with open ('ListaDePares.txt', 'w') as file2:
                for index in (file.read()):
                    index.split()
                    for u in index:
                        a = int(u) % int(u)
                        if a == 0:
                            file2.write(str(int(u)))
                    

NumeroPar('ListaOrdenada.txt')  #Código ejemplo