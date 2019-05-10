import sympy
import sys
import time

for line in sys.stdin:
    fields = line.split(',')
    first_field = int(fields[0])
    if(first_field < 7500 and sympy.isprime(first_field)):
        sys.stdout.write(str(line))