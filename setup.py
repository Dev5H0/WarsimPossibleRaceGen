from sys import exit

class file:
   races = './assets/races.txt'
   p1 = './assets/prefix1.txt'
   p2 = './assets/prefix2.txt'

def ff(t, ft=file.races):
   f = open(ft, t)
   return f

def g(fi=file.races):
   with ff('r', fi) as f:
      data = f.read()

   return data.split('\n')

class arr:
   races = g(file.races)
   p1 = g(file.p1)
   p2 = g(file.p2)

if __name__ == '__main__':
   print(f'{arr.races} \n\n{arr.p1} \n\n{arr.p2} ')
   exit()
