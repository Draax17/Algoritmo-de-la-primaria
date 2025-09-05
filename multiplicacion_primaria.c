#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_DIGITS 1000

// Estructura para representar un número de n dígitos
typedef struct {
    int digitos[MAX_DIGITS];
    int longitud;
} Numero;

// Función para inicializar un número
void inicializar_numero(Numero *num) {
    for (int i = 0; i < MAX_DIGITS; i++) {
        num->digitos[i] = 0;
    }
    num->longitud = 0;
}

// Función para convertir string a número
void string_a_numero(const char *str, Numero *num) {
    inicializar_numero(num);
    int len = strlen(str);
    num->longitud = len;
    
    // Almacenar dígitos en orden inverso (dígito menos significativo en índice 0)
    for (int i = 0; i < len; i++) {
        num->digitos[i] = str[len - 1 - i] - '0';
    }
}

// Función para convertir número a string
void numero_a_string(const Numero *num, char *str) {
    int len = num->longitud;
    for (int i = 0; i < len; i++) {
        str[i] = num->digitos[len - 1 - i] + '0';
    }
    str[len] = '\0';
}

// Función para imprimir un número
void imprimir_numero(const Numero *num) {
    char str[MAX_DIGITS + 1];
    numero_a_string(num, str);
    printf("%s", str);
}

// Función para sumar dos números
Numero sumar_numeros(const Numero *a, const Numero *b) {
    Numero resultado;
    inicializar_numero(&resultado);
    
    int carry = 0;
    int max_len = (a->longitud > b->longitud) ? a->longitud : b->longitud;
    
    for (int i = 0; i < max_len || carry > 0; i++) {
        int suma = carry;
        if (i < a->longitud) suma += a->digitos[i];
        if (i < b->longitud) suma += b->digitos[i];
        
        resultado.digitos[i] = suma % 10;
        carry = suma / 10;
        resultado.longitud = i + 1;
    }
    
    return resultado;
}

// Función para multiplicar un número por un dígito
Numero multiplicar_por_digito(const Numero *num, int digito) {
    Numero resultado;
    inicializar_numero(&resultado);
    
    int carry = 0;
    for (int i = 0; i < num->longitud || carry > 0; i++) {
        int producto = carry;
        if (i < num->longitud) {
            producto += num->digitos[i] * digito;
        }
        
        resultado.digitos[i] = producto % 10;
        carry = producto / 10;
        resultado.longitud = i + 1;
    }
    
    return resultado;
}

// Función para desplazar un número hacia la izquierda (multiplicar por 10^n)
Numero desplazar_izquierda(const Numero *num, int posiciones) {
    Numero resultado;
    inicializar_numero(&resultado);
    
    // Copiar dígitos desplazados
    for (int i = 0; i < num->longitud; i++) {
        resultado.digitos[i + posiciones] = num->digitos[i];
    }
    resultado.longitud = num->longitud + posiciones;
    
    return resultado;
}

// Función principal: multiplicación usando algoritmo de la primaria
Numero multiplicar_primaria(const Numero *a, const Numero *b) {
    Numero resultado;
    inicializar_numero(&resultado);
    
    // Para cada dígito del segundo número (b)
    for (int i = 0; i < b->longitud; i++) {
        // Multiplicar el primer número por el dígito actual de b
        Numero producto_parcial = multiplicar_por_digito(a, b->digitos[i]);
        
        // Desplazar el resultado parcial hacia la izquierda según la posición
        Numero producto_desplazado = desplazar_izquierda(&producto_parcial, i);
        
        // Sumar al resultado total
        Numero nuevo_resultado = sumar_numeros(&resultado, &producto_desplazado);
        resultado = nuevo_resultado;
    }
    
    return resultado;
}

// Función para generar un número aleatorio de n dígitos
Numero generar_numero_aleatorio(int n_digitos) {
    Numero num;
    inicializar_numero(&num);
    
    num.longitud = n_digitos;
    // Primer dígito no puede ser 0
    num.digitos[n_digitos - 1] = (rand() % 9) + 1;
    
    // Resto de dígitos
    for (int i = 0; i < n_digitos - 1; i++) {
        num.digitos[i] = rand() % 10;
    }
    
    return num;
}

// Función para probar la multiplicación
void probar_multiplicacion(int n_digitos) {
    printf("\n=== Prueba con números de %d dígitos ===\n", n_digitos);
    
    Numero a = generar_numero_aleatorio(n_digitos);
    Numero b = generar_numero_aleatorio(n_digitos);
    
    printf("Número A: ");
    imprimir_numero(&a);
    printf("\n");
    
    printf("Número B: ");
    imprimir_numero(&b);
    printf("\n");
    
    Numero resultado = multiplicar_primaria(&a, &b);
    
    printf("Resultado: ");
    imprimir_numero(&resultado);
    printf("\n");
}

// Función para probar con números específicos
void probar_casos_especificos() {
    printf("\n=== Casos de Prueba Específicos ===\n");
    
    // Caso 1: 123 * 456
    Numero a1, b1;
    string_a_numero("123", &a1);
    string_a_numero("456", &b1);
    
    printf("123 * 456 = ");
    Numero resultado1 = multiplicar_primaria(&a1, &b1);
    imprimir_numero(&resultado1);
    printf(" (Esperado: 56088)\n");
    
    // Caso 2: 999 * 999
    Numero a2, b2;
    string_a_numero("999", &a2);
    string_a_numero("999", &b2);
    
    printf("999 * 999 = ");
    Numero resultado2 = multiplicar_primaria(&a2, &b2);
    imprimir_numero(&resultado2);
    printf(" (Esperado: 998001)\n");
    
    // Caso 3: 12 * 34
    Numero a3, b3;
    string_a_numero("12", &a3);
    string_a_numero("34", &b3);
    
    printf("12 * 34 = ");
    Numero resultado3 = multiplicar_primaria(&a3, &b3);
    imprimir_numero(&resultado3);
    printf(" (Esperado: 408)\n");
}

int main() {
    printf("=== Algoritmo de Multiplicación de la Primaria ===\n");
    printf("Implementado en C usando arreglos para números de n dígitos\n");
    
    // Inicializar semilla para números aleatorios
    srand(42);
    
    // Probar casos específicos
    probar_casos_especificos();
    
    // Probar con diferentes potencias de 2
    int potencias[] = {1, 2, 4, 8, 16, 32};
    int num_potencias = sizeof(potencias) / sizeof(potencias[0]);
    
    printf("\n=== Pruebas con Potencias de 2 ===\n");
    for (int i = 0; i < num_potencias; i++) {
        probar_multiplicacion(potencias[i]);
    }
    
    // Prueba adicional con números más grandes
    printf("\n=== Prueba Adicional con Números Grandes ===\n");
    Numero grande1, grande2;
    string_a_numero("12345678901234567890", &grande1);
    string_a_numero("98765432109876543210", &grande2);
    
    printf("Número grande 1: ");
    imprimir_numero(&grande1);
    printf("\n");
    
    printf("Número grande 2: ");
    imprimir_numero(&grande2);
    printf("\n");
    
    printf("Resultado: ");
    Numero resultado_grande = multiplicar_primaria(&grande1, &grande2);
    imprimir_numero(&resultado_grande);
    printf("\n");
    
    return 0;
}
