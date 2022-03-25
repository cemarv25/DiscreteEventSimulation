def congruencial_blum(seed, m, n):
  i = 0
  xn_minus_one = seed
  xn = 0
  results = []
  while (i < n):
    xn = (pow(xn_minus_one, 2)) % m
    ri = xn / (m - 1)
    results.append("{:.5f}".format(ri))

    i += 1
    xn_minus_one = xn

  return results

if __name__ == "__main__":
  seed = int(input('escribe la semilla: '))
  m = int(input('escribe el valor para m: '))

  n = int(input('ahora escribe cuantos numeros quieres generar: '))

  print(congruencial_blum(seed, m, n))