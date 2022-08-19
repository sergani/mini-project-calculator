import calc

print("This calculator will ask you to enter add/sub/mult/div and the numbers.")


while True:
  operation = input('Enter the operation you would like to run (add/sub/mult/div): ')
  x = input('Please enter number 1: ')
  y = input('Please enter number 2: ')
  if operation == "add":
    x = int(x)
    y = int(y)
    z = calc.add(x, y)
    print("Your result: {}".format(z))
  elif operation == "sub":
    x = int(x)
    y = int(y)
    z = calc.sub(x, y)
    print("Your result: {}".format(z))
  elif operation == "mult":
    x = int(x)
    y = int(y)
    z = calc.mult(x, y)
    print("Your result: {}".format(z))
  elif operation == "div":
    x = int(x)
    y = int(y)
    z = calc.div(x, y)
    print("Your result: {}".format(z))
  else:
    print("Incorrect operation given, exiting!")
    break
  
  more_operations = input('Would you like to run another operation? [y] ')
  if more_operations == '':
    more_operations = 'y'
  
  if more_operations == 'y':
    pass
  else:
    print('Thank you, exiting!')
    break
