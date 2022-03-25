def congruencial_mult(seed, k, g, n, a, m):
  if not a:
    a = 5 + 8 * int(k)

  if not m:
    m = pow(2, int(g))

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

  has_a = int(input('se tiene un valor para a? (1= sí, 0= no)'))
  a = None
  if has_a:
    a = input('escribe el valor para a: ')
    
  has_m = int(input('se tiene un valor para m? (1= sí, 0= no)'))
  m = None
  if has_m:
    m = input('escribe el valor para m: ')
    
  n = int(input('ahora escribe cuantos numeros quieres generar: '))

  print(congruencial_mult(seed, k, g, n, a, m))