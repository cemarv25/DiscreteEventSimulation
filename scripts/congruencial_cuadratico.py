def congruencial_cuadr(seed, m, a, b, c, n):
  i = 0
  xn_minus_one = int(seed)
  xn = 0
  results = []
  while (i < n):
    xn = ((a * pow(xn_minus_one, 2)) + (b * xn_minus_one) + c) % m

    ri = xn / (m - 1)
    results.append("{:.5f}".format(ri))

    i += 1
    xn_minus_one = xn

  return results

def menu():
  seed = input('escribe la semilla: ')
  m = int(input('escribe el valor para m: '))
  a = int(input('escribe el valor para a: '))
  b = int(input('escribe el valor para b: '))
  c = int(input('escribe el valor para c: '))

    
  n = int(input('ahora escribe cuantos numeros quieres generar: '))

  print(congruencial_cuadr(seed, m, a, b, c, n))

if __name__ == "__main__":
  menu()