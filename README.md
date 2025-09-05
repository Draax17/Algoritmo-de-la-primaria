# Algoritmo de la Primaria

## 📚 Información del Proyecto

**Materia:** Análisis y Diseño de Algoritmos  
**Grupo:** 3AV1  
**Carrera:** Licenciatura en Ciencia de Datos  
**Institución:** Escuela Superior de Cómputo (ESCOM) - Instituto Politécnico Nacional (IPN)

## 👥 Integrantes del Equipo

- **Fanny Valderrama López**
- **Elena Carmina Mata González**

## 🎯 Descripción

Este repositorio contiene la implementación y análisis del **Algoritmo de la Primaria**, desarrollado como parte de las prácticas de la materia de Análisis y Diseño de Algoritmos. El proyecto incluye la implementación del algoritmo, análisis de complejidad computacional y documentación detallada.

## 📋 Contenido del Repositorio

- [x] Implementación del algoritmo en C
- [x] Casos de prueba con números de n dígitos
- [x] Pruebas con potencias de 2 (1, 2, 4, 8, 16, 32 dígitos)
- [ ] Análisis de complejidad temporal y espacial
- [ ] Documentación técnica
- [ ] Presentación de resultados

## 🚀 Instalación y Uso

### Requisitos
- Compilador de C (gcc recomendado)
- Sistema operativo compatible con C

### Ejecución
```bash
# Clonar el repositorio
git clone https://github.com/[usuario]/Algoritmo-de-la-primaria.git

# Navegar al directorio
cd Algoritmo-de-la-primaria

# Compilar el programa
gcc -o multiplicacion_primaria multiplicacion_primaria.c

# Ejecutar el algoritmo
./multiplicacion_primaria
```

### Características de la Implementación

- **Manejo de números grandes**: Utiliza arreglos para representar números de hasta 1000 dígitos
- **Algoritmo de la primaria**: Implementa el método tradicional de multiplicación
- **Pruebas automáticas**: Incluye casos de prueba con diferentes tamaños de números
- **Potencias de 2**: Prueba específicamente con números de 1, 2, 4, 8, 16 y 32 dígitos

### Estructura del Código

```c
typedef struct {
    int digitos[MAX_DIGITS];
    int longitud;
} Numero;
```

### Funciones Principales

- `multiplicar_primaria()`: Función principal que implementa el algoritmo
- `sumar_numeros()`: Suma dos números representados como arreglos
- `multiplicar_por_digito()`: Multiplica un número por un dígito único
- `desplazar_izquierda()`: Desplaza un número (multiplica por 10^n)

## 📊 Análisis de Complejidad

| Aspecto | Complejidad |
|---------|-------------|
| Tiempo | O(n²) |
| Espacio | O(n) |

## 🧪 Casos de Prueba

El proyecto incluye diversos casos de prueba para validar la correcta implementación del algoritmo:

### Casos Específicos
- 123 × 456 = 56088
- 999 × 999 = 998001
- 12 × 34 = 408

### Números Aleatorios
- Pruebas con números de 1, 2, 4, 8, 16 y 32 dígitos (potencias de 2)
- Números muy grandes: 12345678901234567890 × 98765432109876543210

### Ejemplo de Salida
```
=== Algoritmo de Multiplicación de la Primaria ===
Implementado en C usando arreglos para números de n dígitos

=== Casos de Prueba Específicos ===
123 * 456 = 56088 (Esperado: 56088)
999 * 999 = 998001 (Esperado: 998001)
12 * 34 = 408 (Esperado: 408)
```

## 📈 Resultados

Los resultados del análisis y las pruebas se documentan en el archivo de resultados correspondiente.

## 📝 Documentación

Para más detalles sobre la implementación y el análisis, consulta la documentación técnica incluida en el repositorio.

## 🤝 Contribuciones

Este es un proyecto académico desarrollado por el equipo de estudiantes. Las contribuciones externas no son necesarias, pero se agradecen los comentarios y sugerencias.

## 📄 Licencia

Este proyecto es de carácter académico y está destinado únicamente para fines educativos.

## 📞 Contacto

Para cualquier consulta sobre este proyecto, puedes contactar a los integrantes del equipo:

- **Fanny Valderrama López:** [email@example.com]
- **Elena Carmina Mata González:** [email@example.com]

---

**Instituto Politécnico Nacional**  
**Escuela Superior de Cómputo**  
**Licenciatura en Ciencia de Datos**  
**Grupo 3AV1**

*Desarrollado con ❤️ para el aprendizaje y la excelencia académica*
