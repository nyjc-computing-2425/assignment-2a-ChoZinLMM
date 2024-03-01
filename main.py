num = input('Enter a number (decimal or integer): ')
num1 = num.strip(' ')
num2 = num1.replace('.', '')
num3 = num2.lstrip('0')
sf = len(num3)

print('The number', num, 'has', sf, 'significant figures.')
