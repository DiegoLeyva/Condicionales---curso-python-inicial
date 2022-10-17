# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Comparadores
# Ingrese dos palabras cualesquiera y realice las sigueintes
# comparaciones entre ellas
texto_1 = str(input('Ingrese la primera palabra:\n'))

texto_2 = str(input('Ingrese la segunda palabra:\n'))

# Compare cual de las dos palabras es mayor (alfabéticamente)
# Imprima en pantalla según corresponda
if texto_1 > texto_2:
    print(f'{texto_1} es mayor alfabeticamente que {texto_2}')
elif texto_1 < texto_2:
    print(f'{texto_2} es mayor alfabeticamente que {texto_1}')
else:
    print('Ingreso la misma palabra')

# Compare cual de las dos palabras tiene mayor
# cantidad de letras
# Imprima en pantalla según corresponda
if len(texto_1) > len(texto_2):
    print(f'{texto_1} tiene más letras que {texto_2}')
elif len(texto_1) < len(texto_2):
    print(f'{texto_1} tiene menos letras que {texto_2}')
else:
    print(f'{texto_1} y {texto_2} tienen la misma cantidad de letras.')

# Verifique si la primera letra de la primera palabra
# es mayor a la primera letra de la segunda palabra
# Imprima en pantalla según corresponda
primer_texto_1 = texto_1[0]
primer_texto_2 = texto_2[0]

if primer_texto_1 > primer_texto_2:
    print(f'La primer letra de {texto_1} es mayor que la de {texto_2}')
elif primer_texto_1 < primer_texto_2:    
     print(f'La primer letra de {texto_1} es menor que la de {texto_2}')
else:
    print('Las iniciales son las mismas')

copia_texto_1 = texto_1  # Copia de la variable texto_1

# Verifique que copia_texto_1 es igual a texto_1
# Imprima en pantalla según corresponda
if copia_texto_1 == texto_1:
    print(f'{copia_texto_1} es igual a {texto_1}')

# Verifique que copia_texto_1 es distinta a texto_2
# Imprima en pantalla según corresponda
if copia_texto_1 != texto_1:
    print(f'{copia_texto_1} no es igual a {texto_1}')
else:
    print(f'{copia_texto_1} es igual a {texto_1}')

