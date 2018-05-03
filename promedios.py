programa = True
while programa == True:
    print("\************************************************************")
    print("**   Bienvenido al sistema de captura de calificaciones   **")
    print("**                                                        **")
    print("**                   *** MENU ***                         **")
    print("**                                                        **")
    print("**   1.-Capturar calificaciones                           **")
    print("**   2.-Mostar promedio general                           **")
    print("**   3.-Mostrar promedio de alumno                        **")
    print("**   4.-Vaciar las calificaciones actuales                **")
    print("**   5.-Salir del sistema                                 **")
    print("************************************************************\n")

    opcion = raw_input("Elige la opcion que desees: ")       
    if opcion == "1": 
        no_alumnos = int(raw_input("\nCuantos alumnos quiere evaluar? "))
        calificaciones = {}
        promedio_general = []
        if no_alumnos > 0:
            for alumno in range(0,int(no_alumnos)):
                nombre = raw_input("\nPor favor inserte el nombre del alumno no." + str(alumno) + ": \n")        
                primer_parcial = [0,0,0,0]
                segundo_parcial = [0,0,0,0]
                tercer_parcial = [0,0,0,0]
                for parcial in range(0,3):
                    if parcial == 0:
                        print("\n *** Inserte las calificaciones del primer parcial *** \n")
                        for ponderado in range(0,3):
                            if ponderado == 0:                
                                calificacion = float(raw_input('Inserte calificacion de "Saber-hacer": '))
                                primer_parcial[ponderado] = calificacion
                            elif ponderado == 1:            
                                calificacion = float(raw_input('Inserte calificacion de "Saber": '))
                                primer_parcial[ponderado] = calificacion
                            else:
                                calificacion = float(raw_input('Inserte calificacion de "Ser": '))
                                primer_parcial[ponderado] = calificacion             
                    elif parcial == 1:
                        print("\n *** Inserte las calificaciones del segundo parcial *** \n")
                        for ponderado in range(0,3):
                            if ponderado == 0:                
                                calificacion = float(raw_input('Inserte calificacion de "Saber-hacer": '))
                                segundo_parcial[ponderado] = calificacion
                            elif ponderado == 1:            
                                calificacion = float(raw_input('Inserte calificacion de "Saber": '))
                                segundo_parcial[ponderado] = calificacion
                            else:
                                calificacion = float(raw_input('Inserte calificacion de "Ser": '))
                                segundo_parcial[ponderado] = calificacion                        
                    elif parcial == 2:
                        print("\n *** Inserte las calificaciones del tercer parcial *** \n")
                        for ponderado in range(0,3):
                            if ponderado == 0:                
                                calificacion = float(raw_input('Inserte calificacion de "Saber-hacer": '))
                                tercer_parcial[ponderado] = calificacion
                            elif ponderado == 1:            
                                calificacion = float(raw_input('Inserte calificacion de "Saber": '))
                                tercer_parcial[ponderado] = calificacion
                            else:
                                calificacion = float(raw_input('Inserte calificacion de "Ser": '))
                                tercer_parcial[ponderado] = calificacion

                calificaciones[nombre] = [primer_parcial,segundo_parcial,tercer_parcial,]
                primer_parcial[3] = (primer_parcial[0]*.5) + (primer_parcial[1] *.3) + (primer_parcial[2] *.2)
                segundo_parcial[3] = ((segundo_parcial[0]*.5) + (segundo_parcial[1] *.3) + (segundo_parcial[2] *.2))
                tercer_parcial[3] = ((tercer_parcial[0]*.5) + (tercer_parcial[1] *.3) + (tercer_parcial[2] *.2))

                promedio_general.append((primer_parcial[3] + segundo_parcial[3] + tercer_parcial[3])/3)
                print(promedio_general)

            no_alumnos -= 1
            print calificaciones
        else:
            print("Por favor inserte valores validos")
    elif opcion == "2":   
        promedio = 0
        if len(promedio_general) == 1:
            print(promedio_general[0])             
        else:
            for posicion in range(0,len(promedio_general)):
                promedio += promedio_general[posicion]         
            print("\nEl promedio general de este grupo es: \n")                
            print(promedio/len(promedio_general))    
    elif opcion == "3":
        busqueda = raw_input("\nQue alumno deseea consultar? ")
        if busqueda in calificaciones:
            for parcial in range (0,3):                
                if parcial == 0:
                    print("\nPromedio del primer parcial\n")
                    print (calificaciones[busqueda][parcial][3])                            
                elif parcial == 1:
                    print("\nPromedio del segundo parcial\n")
                    print (calificaciones[busqueda][parcial][3])
                elif parcial == 2:
                    print("\nPromedio del tercer parcial\n")
                    print (calificaciones[busqueda][parcial][3])
        else: 
            print("El alumno no existe, verifique que este bien escrito")                
    elif opcion == "4":
        calificaciones = {}
        promedio = 0
        print("\nSe han eliminado las calificaciones anteriores con exito\n")
    elif opcion == "5":
        print("\nHasta luego! :)\n")
        programa = False
    else:
        print("\nOpcion no valida, vuelva a intentarlo\n")