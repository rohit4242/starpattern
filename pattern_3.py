'''
* * * * *  
* * * *  
* * *  
* *  
*  

'''

# Printing Downward half - Pyramid

n = int(input('Enter the your r5ow: '))
for row in range(n,0,-1):
    for col in range(0, row-1):
        print('*', end=' ')
    print()