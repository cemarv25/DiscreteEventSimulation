def congruencial_mult(seed, k, g, n, a, m):
  if not a:
    a = 5 + 8 * int(k)

  if not m:
    m = pow(2, int(g))

  i = 0
  xn_minus_one = seed
  xn = 0
  results = []
  loop = True
  while (loop):
    xn = (int(a) * int(xn_minus_one)) % int(m)
    ri = xn / (int(m) - 1)
    ri_formatted = "{:.5f}".format(ri)
    

    i += 1
    xn_minus_one = xn

    if n > 0:
      loop = i < n
    else:
      loop = ri_formatted not in results

    results.append(ri_formatted)
  
  print('numeros generados: ', i)
  return results


def menu():
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

  return congruencial_mult(seed, k, g, n, a, m)

if __name__ == "__main__":
  menu()