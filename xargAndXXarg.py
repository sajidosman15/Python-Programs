#XArgs
def sum(*num):
    sum=0
    for i in num:
        sum=sum+i
    return sum

print(sum(3,4))
print(sum(3,4,5))

#XXArgs
def display(**info):
    print(info["id"])
    print(info["name"])

display(id=102,name="sajid")