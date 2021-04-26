from datetime import datetime

#comprime un string, si el string comprimido no es más corto que el original, entonces retorna el original
def compressString(string1 = ''):
  try:
    if not (isinstance(string1, str)):
      raise TypeError('no se ha entregado un string')
    ahora = datetime.now()
    date = '{ ' + '"fecha": "{}" , '.format(ahora)

    compressedString = ''
    counter = 0
    charCounter = 1
    char = ''
    for character in string1:
      #print(compressedString)
      if counter == 0:
        char = character
        counter = counter + 1
      else:
        if character == char:
          charCounter = charCounter+ 1
        else:
          compressedString = compressedString + char
          compressedString =  compressedString + str(charCounter)
          char = character
          charCounter = 1
    compressedString = compressedString + char
    compressedString =  compressedString + str(charCounter)

    output = ''
    if len(compressedString) >= len(string1):
      print('output: ', string1)
      output = string1
    else:
      print('output: ',compressedString)
      output = compressedString

    logMaker(date, string1, compressedString, output)

  except TypeError as err:
    output = "ERROR, " + str(err)
    logMaker(date, string1, compString, output, 1)

  except KeyboardInterrupt as err:
    output = "ERROR, "+ str(err)
    logMaker(date, string1, compString, output, 1)

  except MemoryError as err:
    output = "ERROR, " + str(err)
    logMaker(date, string1, compString, output, 1)

def logMaker(date, string1, compString, output,  err = 0):
  try:
    file = open('log_tarea1_iei235.txt', 'a', encoding="utf-8")
  except OSError() as err:
    log = "WARNING, " + str(err)
    print(log)
    return 0
  else:
    log = ""
    if err == 0:
      log = date + '"string": "{}" , "compressedString": "{}" , "output": "{}" '.format(string1, compString, output) + ' }\n'
      log.encode('utf-8')
      file.write(log)
      file.close()
    else:
      print(output)
      log = date + '"string": "{}" , "compressedString": "{}" , "output": "{}" '.format(string1, compString, output) + ' }\n'
      log.encode('utf-8')
      file.write(log)
      file.close()
      return 1

stoper = ''
while stoper != 'X' and stoper != 'x':
  str1 = input('Ingrese cadena: ')
  while len(str1) < 1:
    str1 = input('Ingrese cadena: ')

  compressString(str1)
  stoper = input('ENTER para repetir, o escriba X para salir.')
