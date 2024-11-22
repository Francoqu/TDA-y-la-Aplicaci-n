# Evaluador de Expresiones Matemáticas

## Descripción

Este proyecto implementa un Tipo Abstracto de Datos (TDA) **Pila** en Python, que se utiliza para crear una aplicación simple: un evaluador de expresiones matemáticas.  
La aplicación permite convertir expresiones en notación infija a notación postfija (notación polaca inversa) y posteriormente evaluarlas para obtener el resultado.

## Características

- Implementación del TDA Pila con operaciones básicas: `push`, `pop`, `peek`, `is_empty`.
- Conversión de expresiones matemáticas de notación infija a notación postfija.
- Evaluación de expresiones en notación postfija.

## Requisitos

- Python 3.x instalado en tu sistema.

## Instalación

1. Clona este repositorio:
    ```bash
    git clone https://github.com/tuusuario/evaluador-expresiones.git
    cd evaluador-expresiones
    ```
2. Ejecuta el programa:
    ```bash
    python main.py
    ```

## Uso

1. Al ejecutar el programa, se te pedirá que introduzcas una expresión matemática en formato infijo. Ejemplo de entrada:
    ```
    ( 3 + 5 ) * 2
    ```
2. El programa convertirá la expresión a notación postfija y la evaluará. Ejemplo de salida:
    ```
    Notación postfija: 3 5 + 2 *
    Resultado: 16
    ```

## Ejemplo Completo

**Entrada:**
