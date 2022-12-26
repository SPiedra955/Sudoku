def checkColumns(sudoku):
    
    assert isinstance(sudoku, list)
    
    first_row = sudoku[0]

    number_of_rows = len(sudoku) - 1

    for number in first_row:

        rowCurrentIndex = 0
        
        # Buscamos cada elemento de la primera fila en el resto de filas:
        # Si el indice que ocupa en las otras filas es igual al que ocupa en la primera: mal <=>
        # <=> no puede haber dos numeros iguales en la misma columna.
         
        while rowCurrentIndex < number_of_rows:
            
            nextIndexRow = rowCurrentIndex + 1

            try:
                # El elemento puede no existir en la fila siguiente: 
                # index devuelve excepcion: ValueError = mensaje "x is not in list"
                # Imposible alcanzar esta excepcion si checkColumnas se ejecuta despues de checkFilas
                positionNumberNextRow = sudoku[nextIndexRow].index(number)
        
            except ValueError:
                    # Este bloque de codigo se ejecuta si sudoku[indexFilaSiguiente].index(numero)
                    # devuelve un error <=> si el numero no esta en la fila siguiente
                    # no llegaria a presentarse el caso pues checkNumerosEnRango se ejecuta antes
                return False
            
            else:
                if positionNumberNextRow == first_row.index(number):
                    return False
                else:
                    rowCurrentIndex += 1
    return True
