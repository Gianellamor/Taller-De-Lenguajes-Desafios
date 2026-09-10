#Escribir una función reciba una lista de notas y devuelva la lista de calificaciones correspondientes a esas notas
def lista_calificaciones(notas):
    calificaciones = []
    for notas in nota:
        if notas < 4:
          calificaciones.append ("Desaprobado")
         
        elif notas <= 7 :
          calificaciones.append ("Aprobado")
         
        elif notas <= 10:
          calificaciones.append ("Sobresaliente")
          
        else :
          return "La nota no es valida"
    return calificaciones

nota = [3,5,6,4.5,7,10,8,1]
resultado = lista_calificaciones(nota)

print(resultado)