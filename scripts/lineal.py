def lineal(seed, a, c, m, n):
  i = 0
  xn = seed
  results = []
  loop = True
  while (loop):
    xn = (int(a) * int(xn) + int(c)) % int(m)
    ri = xn / (int(m) - 1)
    ri_formatted = "{:.5f}".format(ri)
    results.append(ri_formatted)

    i += 1

    if n > 0:
      loop = i < n
    else:
      loop = ri_formatted in results
      print('loop: ', loop)
  
  print('numeros generados: ', i)
  return results


def menu():
  seed = input('escribe la semilla: ')
  a = input('escribe el valor para a: ')
  c = input('escribe el valor para c: ')
  m = input('escribe el valor para m: ')
  n = int(input('ahora escribe cuantos numeros quieres generar: '))

  return lineal(seed, a, c, m, n)

if __name__ == "__main__":
  menu()