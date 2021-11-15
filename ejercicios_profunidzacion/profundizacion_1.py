# Tipos de variables [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un calculadora, se ingresará por línea de comando dos
números reales y se deberá calcular todas las operaciones entre ellos:
A) Suma
B) Resta
C) Multiplicación
D) División
E) Exponente/Potencia

- Para todos los casos se debe imprimir en pantalla el resultado aclarando
  la operación realizada en cada caso y con que números
  se ha realizado la operación
  ej: La suma entre 4.2 y 6.5 es 10.7
'''

print('¡Nuestra primera calculadora!')

print('Ingrese el primer numero')
numero1 = float(input())
print('Ingrese el segundo numero')
numero2 = float(input())

suma = numero1 + numero2
print('La suma entre:', numero1, 'y', numero2 , 'es:', suma)

resta = numero1 - numero2
print('La resta entre:', numero1, 'y', numero2 , 'es:', resta)

multiplicacion = numero1 * numero2
print('La multiplicacion entre:', numero1, 'y', numero2 , 'es:', multiplicacion)

division = numero1 / numero2
print('La division entre:', numero1, 'y', numero2 , 'es:', division)

potencia = numero1 ** numero2
print('El exponente entre:', numero1, 'y', numero2 , 'es:', potencia)