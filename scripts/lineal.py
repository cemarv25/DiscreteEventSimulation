def lineal(seed, a, c, m, n):
  i = 0
  xn = seed
  results = []
  while (i < n):
    xn = (int(a) * int(xn) + int(c)) % int(m)
    ri = xn / (int(m) - 1)
    
    results.append(ri)

    i += 1
  
  return results


if __name__ == "__main__":
  seed = input('escribe la semilla: ')
  a = input('escribe el valor para a: ')
  c = input('escribe el valor para c: ')
  m = input('escribe el valor para m: ')
  n = int(input('ahora escribe cuantos numeros quieres generar: '))

  print(lineal(seed, a, c, m, n))