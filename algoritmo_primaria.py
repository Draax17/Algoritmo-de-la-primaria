"""
Algoritmo de Multiplicación de la Primaria
Implementación usando arreglos/listas en Python

Este programa implementa el algoritmo tradicional de multiplicación que se enseña
en la escuela primaria, usando listas para representar números de n dígitos.
"""

def numero_a_lista(numero):
    """
    Convierte un número entero a una lista de dígitos.
    
    Args:
        numero (int): Número entero a convertir
        
    Returns:
        list: Lista de dígitos (del más significativo al menos significativo)
    """
    if numero == 0:
        return [0]
    
    digitos = []
    while numero > 0:
        digitos.insert(0, numero % 10)  # Insertar al inicio para mantener orden
        numero //= 10
    
    return digitos


def lista_a_numero(lista_digitos):
    """
    Convierte una lista de dígitos a un número entero.
    
    Args:
        lista_digitos (list): Lista de dígitos
        
    Returns:
        int: Número entero resultante
    """
    numero = 0
    for digito in lista_digitos:
        numero = numero * 10 + digito
    return numero


def suma_listas(lista1, lista2):
    """
    Suma dos números representados como listas de dígitos.
    
    Args:
        lista1 (list): Primer número como lista de dígitos
        lista2 (list): Segundo número como lista de dígitos
        
    Returns:
        list: Resultado de la suma como lista de dígitos
    """
    # Asegurar que ambas listas tengan la misma longitud
    max_len = max(len(lista1), len(lista2))
    lista1 = [0] * (max_len - len(lista1)) + lista1
    lista2 = [0] * (max_len - len(lista2)) + lista2
    
    resultado = []
    carry = 0
    
    # Sumar de derecha a izquierda
    for i in range(max_len - 1, -1, -1):
        suma = lista1[i] + lista2[i] + carry
        resultado.insert(0, suma % 10)
        carry = suma // 10
    
    # Si queda carry al final
    if carry > 0:
        resultado.insert(0, carry)
    
    return resultado


def multiplicar_digito_por_lista(digito, lista_numero, posicion):
    """
    Multiplica un dígito por un número representado como lista.
    
    Args:
        digito (int): Dígito a multiplicar (0-9)
        lista_numero (list): Número como lista de dígitos
        posicion (int): Posición para agregar ceros al final
        
    Returns:
        list: Resultado de la multiplicación como lista de dígitos
    """
    if digito == 0:
        return [0]
    
    resultado = []
    carry = 0
    
    # Multiplicar de derecha a izquierda
    for i in range(len(lista_numero) - 1, -1, -1):
        producto = digito * lista_numero[i] + carry
        resultado.insert(0, producto % 10)
        carry = producto // 10
    
    # Si queda carry al final
    if carry > 0:
        resultado.insert(0, carry)
    
    # Agregar ceros según la posición
    resultado.extend([0] * posicion)
    
    return resultado


def multiplicar_primaria(numero1, numero2):
    """
    Multiplica dos números usando el algoritmo de la primaria.
    
    Args:
        numero1 (int): Primer número a multiplicar
        numero2 (int): Segundo número a multiplicar
        
    Returns:
        int: Resultado de la multiplicación
    """
    # Convertir números a listas de dígitos
    lista1 = numero_a_lista(numero1)
    lista2 = numero_a_lista(numero2)
    
    print(f"Multiplicando: {lista_a_numero(lista1)} × {lista_a_numero(lista2)}")
    print(f"Lista 1: {lista1}")
    print(f"Lista 2: {lista2}")
    print("-" * 50)
    
    resultados_parciales = []
    
    # Para cada dígito del segundo número (de derecha a izquierda)
    for i, digito in enumerate(reversed(lista2)):
        posicion = i  # Posición para agregar ceros
        resultado_parcial = multiplicar_digito_por_lista(digito, lista1, posicion)
        resultados_parciales.append(resultado_parcial)
        
        print(f"Multiplicando por {digito} (posición {posicion}): {resultado_parcial}")
    
    print("-" * 50)
    
    # Sumar todos los resultados parciales
    resultado_final = [0]
    for resultado_parcial in resultados_parciales:
        resultado_final = suma_listas(resultado_final, resultado_parcial)
    
    print(f"Sumando resultados parciales...")
    for i, parcial in enumerate(resultados_parciales):
        print(f"  + {parcial}")
    print(f"Resultado: {resultado_final}")
    
    # Convertir resultado final a número
    return lista_a_numero(resultado_final)


def generar_numero_potencia_2(digitos):
    """
    Genera un número aleatorio con el número especificado de dígitos.
    
    Args:
        digitos (int): Número de dígitos deseado
        
    Returns:
        int: Número aleatorio con el número especificado de dígitos
    """
    import random
    
    # Generar el primer dígito (no puede ser 0)
    primer_digito = random.randint(1, 9)
    
    # Generar los dígitos restantes
    numero_str = str(primer_digito)
    for _ in range(digitos - 1):
        numero_str += str(random.randint(0, 9))
    
    return int(numero_str)


def probar_algoritmo():
    """
    Función principal para probar el algoritmo con diferentes números.
    """
    print("=" * 60)
    print("ALGORITMO DE MULTIPLICACIÓN DE LA PRIMARIA")
    print("=" * 60)
    print()
    
    # Casos de prueba con diferentes potencias de 2
    potencias = [1, 2, 4, 8]  # Números de 1, 2, 4 y 8 dígitos
    
    for potencia in potencias:
        print(f"\n{'='*20} PRUEBA CON NÚMEROS DE {potencia} DÍGITOS {'='*20}")
        
        # Generar números aleatorios
        num1 = generar_numero_potencia_2(potencia)
        num2 = generar_numero_potencia_2(potencia)
        
        print(f"\nNúmeros generados:")
        print(f"Número 1: {num1}")
        print(f"Número 2: {num2}")
        print()
        
        # Ejecutar el algoritmo
        resultado_algoritmo = multiplicar_primaria(num1, num2)
        resultado_real = num1 * num2
        
        print(f"\nResultado del algoritmo: {resultado_algoritmo}")
        print(f"Resultado real (verificación): {resultado_real}")
        print(f"¿Coinciden? {'✅ SÍ' if resultado_algoritmo == resultado_real else '❌ NO'}")
        
        print("\n" + "="*80)


def probar_casos_especificos():
    """
    Prueba casos específicos para verificar la corrección del algoritmo.
    """
    print("\n" + "="*60)
    print("PRUEBAS CON CASOS ESPECÍFICOS")
    print("="*60)
    
    casos_prueba = [
        (12, 13),
        (123, 456),
        (999, 999),
        (1000, 2000),
        (12345, 67890)
    ]
    
    for num1, num2 in casos_prueba:
        print(f"\n{'='*20} CASO: {num1} × {num2} {'='*20}")
        
        resultado_algoritmo = multiplicar_primaria(num1, num2)
        resultado_real = num1 * num2
        
        print(f"\nResultado del algoritmo: {resultado_algoritmo}")
        print(f"Resultado real: {resultado_real}")
        print(f"¿Coinciden? {'✅ SÍ' if resultado_algoritmo == resultado_real else '❌ NO'}")


if __name__ == "__main__":
    # Ejecutar las pruebas
    probar_algoritmo()
    probar_casos_especificos()
    
    print("\n" + "="*60)
    print("PROGRAMA TERMINADO")
    print("="*60)
