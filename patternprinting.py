'''
*
**
***
****
*****
'''

for x in range(6):
    for y in range(x):
        print("*",end=" ")
    print()

'''
   *
  ***
 *****
*******
'''
n=4
for i in range(n):
    for k in range(n-i-1):
        print(" ",end=" ")
    for j in range((i*2)+1):
        print("*",end=" ")
    print()

#shortcut

for i in range(n):
    print((n-i-1)*" ",end="")
    print((i*2+1)*"*")