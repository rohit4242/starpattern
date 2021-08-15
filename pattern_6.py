'''

* * * * * * * * * * * 
  * * * * * * * * * 
    * * * * * * * 
      * * * * * 
        * * * 
          *

'''

# Downward Pyramid Pattern Program

n = int(input('Enter the your row: '))
for row in range(n, 0, -1):
    for col in range(n-row):
        print(end=' ')
    for k in range(row):
        print('*', end=' ')
        
    print()
