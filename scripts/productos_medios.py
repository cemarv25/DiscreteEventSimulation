import scripts.shared

def productos_medios(seed1, seed2, n):
  i = 0
  D = len(seed1)
  xn = seed1
  xn2 = seed2
  results = []
  while(i < n):
    yn = int(xn) * int(xn2)
    if len(str(yn)) < D:
      raise scripts.shared.NoMoreMiddleDigits('Ya no se pudieron generar nuevos numeros')

    xn = xn2
    xn2 = scripts.shared.get_middle_digits(str(yn), D)

    results.append("0." + xn2)

    i += 1

  return results


def menu():
  valid_seed = False
  while(not valid_seed):
    seed1 = input('escribe la primer semilla (minimo 3 digitos): ')
    seed2 = input('escribe la segunda semilla (misma cantidad de digitos que la primer semilla): ')

    if len(seed1) >= 3 and len(seed2) == len(seed1):
        valid_seed = True


  n = int(input('ahora escribe cuantos numeros quieres generar: '))

  try:
    print(productos_medios(seed1, seed2, n))
  except scripts.shared.NoMoreMiddleDigits as e:
    msg, vals = e.args
    print(msg, vals)

if __name__ == '__main__':
  menu()
