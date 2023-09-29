#Author: Jacob Neaderland
import math
import time
x = time.process_time()
a = math.pow(2, 4)
y = time.process_time()
b = math.pow (2, 2)
z = time.process_time()
c = math.pow (2, 1)
d = time.process_time()
print (a + b + c)
print (x + y + z + d)
#It ran in 0.25 which is very quick
x = time.perf_counter()
a = math.pow(2, 4)
y = time.perf_counter()
b = math.pow (2, 2)
z = time.perf_counter()
c = math.pow (2, 1)
d = time.perf_counter()
print (a + b + c)
print (x + y + z + d)
#The nuber is now 680910.6293561001 which is much larger than 0.25