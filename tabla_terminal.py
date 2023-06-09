def show_board():
    print("| Día de la semana | Actividad |")
    print("--------------------------------")
    days = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    activities = {}

    day_width = max([len(day) for day in days]) + 2
    activity_width = 12  # Ancho inicial de la columna de actividad
    
    # Imprimir cada día de la semana en una fila de la tabla
    for day in days:
        if day in activities:
            activities = activities[day]
        else:
            activities = ""

        # Ajustar dinámicamente el ancho de la columna de actividad si es necesario
        activity_width = max(activity_width, len(activities) + 2)

        print(f"| {day:<{day_width}} | {activities:<{activity_width}} |")
        print("--------------------------------")
    
    for day in days:
        answer = input(f"Ingrese una actividad para el {day}: ")
        activities[day] = answer
        
        # Actualizar la tabla después del ingreso del dato
        print("| Día de la semana | Actividad |")
        print("--------------------------------")
        for day in days:
            if day in activities:
                activities = activities[day]
            else:
                activities = ""
            print(f"| {day:<{day_width}} | {activities:<{activity_width}} |")
            print("--------------------------------")

show_board()
