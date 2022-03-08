def aditivo(xs, m, n, j):
  i = len(xs)
  xn = 0
  results = []
  while (i < int(n) + int(j)):
    xi_minus_one = xs[i - 1]
    xi_minus_n = xs[i - int(n)]
    xn = (int(xi_minus_one) + int(xi_minus_n)) % int(m)
    ri = xn / (int(m) - 1)
    
    results.append("{:.5f}".format(ri))
    xs.append(xn)

    i += 1
  
  return results


if __name__ == "__main__":
  n = input('cuantas xn hay? ')
  xs = []
  for i in range(int(n)):
    xs.append(input(f'escribe el valor de la x {i + 1}: '))
  m = input('ahora escribe el valor de m: ')
  j = input('cuantos numeros quieres generar? ')
  print(aditivo(xs, m, n, j))