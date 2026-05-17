

# Definimos la matriz de empleados y sus horas diarias
empleados = [
    ["Juan", 8, 9, 8, 10, 7],
    ["Maria", 9, 10, 9, 8, 8],
    ["Pedro", 7, 8, 7, 8, 7],
    ["Ana", 10, 10, 10, 10, 10]
]

def calcular_horas_trabajadas(lista_empleados):
    print(f"{'EMPLEADO':<10} | {'TOTAL HORAS':<12} | {'ESTADO'}")
    print("-" * 45)
    
    for fila in lista_empleados:
        nombre = fila[0]
        horas = fila[1:]  # Toma los números (del índice 1 al final)
        total = sum(horas) # Suma automática
        
        if total > 40:
            estado = "Sobretiempo"
        else:
            estado = "Horario Estándar" # Lo ajusté según tu imagen
            
        print(f"{nombre:<10} | {total:<12} | {estado}")

# Llama a la función directamente para evitar errores de guiones
calcular_horas_trabajadas(empleados)

