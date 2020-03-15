import math

def binsearch(arr, l, r, f):
    if(r>l):
        mid = l + math.floor((r - l)/2)
        if(f == arr[mid]):
            print("Found")
            return 0
        elif(f > arr[mid]):
            return binsearch(arr, mid + 1, r, f);
        else:
            return binsearch(arr, l, mid - 1, f);
    else:
        print("Not Found")
        return -1

i = int(input("Enter the number of items in list :"))
x = [0 for m in range(i)];
a = 0
while(a<i):
    x[a] = int(input("Enter element {0}".format(a)))
    a+=1
print("Successfully added all elements")
ele = int(input("Enter the element you want to search in the list :"))
binsearch(x, 0, len(x), ele)