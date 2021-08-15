'''

* * * * * * * 
  * * * * * * 
    * * * * * 
      * * * * 
        * * * 
          * * 
            * 

'''

# Printing Downward left-half - Pyramid

n = int(input('Enter the your row: '))
for row in range(n, 0, -1):
    for col in range(0, n-row):
        print(' ', end=' ')
    for k in range(1, row+1):
        print('*', end=' ')
    print()
