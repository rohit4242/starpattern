'''

            * 
          * * * 
        * * * * * 
      * * * * * * * 
    * * * * * * * * * 
  * * * * * * * * * * * 

'''

# Pyramid Pattern Program

n = int(input('Enter the your row: '))
for row in range(n):
    for col in range(n-row):
        print(' ', end=' ')
    for k in range((2*row)+1):
        print('*', end=' ')
    print()