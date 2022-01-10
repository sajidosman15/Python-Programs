from array import *

arr=array("i",[1,2,3,4,5])
arr.append(6)

for x in arr:
    print(x,end=" ")
print()
i=0
while i<len(arr):
    print(arr[i],end=" ")
    i+=1