import math

x = int(input('Введіть значення х:\n х = '))
y = math.atan(x)+(math.exp(0.6*x-1)-math.sqrt(math.pow((x+6.1),3)))/(math.log(x)+math.pow(math.tan(x),2))
print(y)
