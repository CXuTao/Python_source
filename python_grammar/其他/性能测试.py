import time

time.clock()
sum = 0
for i in range(100000000):
    sum +=i
print(time.clock())