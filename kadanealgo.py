def kadane(array,size):
    max_so_far= array[0]
    max_ending = array[0]
    for i in range(1,size):

        if array[i] < max_ending + array[i]:
            max_ending += array[i]
        else:
            max_ending = array[i]
        if max_ending > max_so_far:
            max_so_far = max_ending
    return max_so_far

t = int(input("enter the test cases: "))
for i in range(t):
    size = int(input("Enter the size: "))
    array = list(map(int, input("enter the array: ").strip().split()))

    print(kadane(array,size))
    
    #addded repo 
