from shared import get_middle_digits, NoMoreMiddleDigits

def mult_constante(seed, a, n):
  i = 0
  D = len(seed)
  xn = seed
  results = []
  while (i < n):
    yn = int(xn) * int(a)
    if len(str(yn)) < D:
      raise NoMoreMiddleDigits('Ya no se pudieron generar nuevos numeros, regresando los posibles', results)
    
    xn = get_middle_digits(str(yn), D)
    
    results.append("0." + xn)

    i += 1
  
  return results

if __name__ == "__main__":
  valid_seed = False
  while(not valid_seed):
    seed = input('escribe la semilla (mayor a 3 digitos): ')
    a = input('escribe el valor de a: ')
    if(len(seed) >= 3):
      valid_seed = True

  n = int(input('ahora escribe cuantos numeros quieres generar: '))

  try:
    print(mult_constante(seed, a, n))
  except NoMoreMiddleDigits as e:
    msg, vals = e.args
    print(msg, vals)