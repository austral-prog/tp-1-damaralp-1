def time():
    """
    Ejercicio 4 - Calculadora de Tiempo

    Dado un total de segundos, calcular e imprimir:
    1. Horas completas
    2. Minutos completos restantes
    3. Segundos restantes
    """
    total_segundos = 3665

    horas= total_segundos/3600
    horas_completas = int(horas)

    minutos= total_segundos/60
    minutos_completos = int(minutos)

    print(horas)
    print(minutos - minutos_completos)
    print(horas - (minutos_completos * 60))
    
time()
