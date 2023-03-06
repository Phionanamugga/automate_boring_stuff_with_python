# imports a random integer
import random
for i in range(5):
    print(random.randint(1, 10))

#imports for modules
import random, sys, os, math

#exit statement from sys
import sys

while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')
