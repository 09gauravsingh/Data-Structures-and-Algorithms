def linear_search(lis, n):
    if n in lis:
        return True
    else:
        return False


user = input("enter the values of list:").split(' ')
list=[int(x) for x in list]
print("list is", lis)

n = int(input())
if linear_search(lis, n):
    print("found")
else:
    print("not found")
