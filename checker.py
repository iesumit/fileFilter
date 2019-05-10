import sympy
import sys
import time

with open("my_pipe", "r", encoding="utf-8") as f:
    print('have opened pipe, commencing reading....')
    while True:
        line = f.readline()
        if line:
            fields = line.split(',')
            first_field = int(fields[0])
            if(first_field < 7500 and sympy.isprime(first_field)):
                sys.stdout.write(str(line))
                time.sleep(1)
        else:
            break
