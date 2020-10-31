t = int(input("enter the test cases: "))

for i in range(t):
    size = int(input("Enter the size: "))
    array = list(map(int, input("enter the array: ").strip().split()))

# Moore's voting algorithm
    maj_index = 0
    count = 1
    for i in range(size):
        if array[maj_index] == array[i]:
         count +=1
        else:
            count -=1
        if count == 0:
            maj_index = i
            count =1
        cand = array[maj_index]
    count = 0
    for i in range(size):
        if array[i]==cand:
            count += 1
    if count > size/2:
        print(cand)
    else:
        print(-1)
