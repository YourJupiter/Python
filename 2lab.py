import math

start = 2.5
step = 0.4
finish = 6.9
t = start

while t <= finish :
  z = (t+math.sin(2*t))/(math.pow(t,2)-3)
  print('z = ', z)
  t += step
