from scripts import productos_medios, cuadrados_medios, mult_constante, lineal, congruencial_mult, aditivo, congruencial_cuadratico, congruencial_blum

menu = """
que generador quieres usar? (escribe el numero de la opcion)
1. productos medios
2. cuadrados medios
3. multiplicacion constante

4. lineal
5. congruencial multiplicativo
6. congruencual aditivo
7. congruencial cuadratico
8. congruencial blum blum
"""


if __name__ == '__main__':
  option = int(input(menu))

  if option == 1:
    productos_medios.menu()
  if option == 2:
    cuadrados_medios.menu()
  if option == 3:
    mult_constante.menu()
  if option == 4:
    resultados = lineal.menu()
    for ri in resultados:
        print(ri)
  if option == 5:
    congruencial_mult.menu()
  if option == 6:
    aditivo.menu()
  if option == 7:
    congruencial_cuadratico.menu()
  if option == 8:
    congruencial_blum.menu()
