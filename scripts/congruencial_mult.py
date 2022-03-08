def congruencial_mult(seed, k, g, a, m, n):
  i = 0
  xn_minus_one = seed
  xn = 0
  results = []
  while (i < n):
    xn = (int(a) * int(xn_minus_one)) % int(m)
    ri = xn / (int(m) - 1)
    
    results.append("{:.5f}".format(ri))

    i += 1
    xn_minus_one = xn
  
  return results


if __name__ == "__main__":
  seed = input('escribe la semilla: ')
  k = input('escribe el valor para k: ')
  g = input('escribe el valor para g: ')
  a = input('escribe el valor para a: ')
  m = input('escribe el valor para m: ')
  n = int(input('ahora escribe cuantos numeros quieres generar: '))

  print(congruencial_mult(seed, k, g, a, m, n))