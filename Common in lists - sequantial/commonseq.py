import random

l1 = list(range(100))
random.shuffle(l1)

l2 = list(range(50))
random.shuffle(l2)

count = 0;
for i in l1:
    for j in l2:
        if i == j:
            print(i)
            count+=1;
print("No of common elements:", count)