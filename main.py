import itertools as iter 
from setup import arr, exit
from os import system

x = [1,2,3,'Hello','World','Test','5H0']


len1 = len(arr.races)
len2 = len(arr.p1)
len3 = len(arr.p2)

file_path = './output/output.txt'

def ff(t='w'):
   f = open(file_path, t)
   return f

x = ''

for n1 in range(0, len1):
   for n2 in range(0, len2):
      for n3 in range(0, len3):
         x = x+(f'{arr.p1[n2]} {arr.p2[n3]} {arr.races[n1]}\n')
         print(f'{arr.p1[n2]} {arr.p2[n3]} {arr.races[n1]}')

with ff() as f:
   f.write(x)

if __name__ == '__main__':
   print('\n(This closes the window.)')
   system('pause')
   f.close()
   exit()