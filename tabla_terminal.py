def mostrar_tabla():
    print("| Día de la semana | Actividad |")
    print("--------------------------------")
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    actividades = {}

    ancho_dia = max([len(dia) for dia in dias_semana]) + 2
    ancho_actividad = 12  # Ancho inicial de la columna de actividad
    
    # Imprimir cada día de la semana en una fila de la tabla
    for dia in dias_semana:
        if dia in actividades:
            actividad = actividades[dia]
        else:
            actividad = ""

        # Ajustar dinámicamente el ancho de la columna de actividad si es necesario
        ancho_actividad = max(ancho_actividad, len(actividad) + 2)

        print(f"| {dia:<{ancho_dia}} | {actividad:<{ancho_actividad}} |")
        print("--------------------------------")
    
    for dia in dias_semana:
        respuesta = input(f"Ingrese una actividad para el {dia}: ")
        actividades[dia] = respuesta
        
        # Actualizar la tabla después del ingreso del dato
        print("| Día de la semana | Actividad |")
        print("--------------------------------")
        for dia in dias_semana:
            if dia in actividades:
                actividad = actividades[dia]
            else:
                actividad = ""
            print(f"| {dia:<{ancho_dia}} | {actividad:<{ancho_actividad}} |")
            print("--------------------------------")

mostrar_tabla()
