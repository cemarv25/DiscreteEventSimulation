import scripts.shared

def mult_constante(seed, a, n):
  i = 0
  D = len(seed)
  xn = seed
  results = []
  while (i < n):
    yn = int(xn) * int(a)
    if len(str(yn)) < D:
      raise scripts.shared.NoMoreMiddleDigits('Ya no se pudieron generar nuevos numeros, regresando los posibles', results)
    
    xn = scripts.shared.get_middle_digits(str(yn), D)
    
    results.append("0." + xn)

    i += 1
  
  return results

def menu():
  valid_seed = False
  while(not valid_seed):
    seed = input('escribe la semilla (mayor a 3 digitos): ')
    a = input('escribe el valor de a: ')
    if(len(seed) >= 3):
      valid_seed = True

  n = int(input('ahora escribe cuantos numeros quieres generar: '))

  try:
    print(mult_constante(seed, a, n))
  except scripts.shared.NoMoreMiddleDigits as e:
    msg, vals = e.args
    print(msg, vals)

if __name__ == "__main__":
  menu()