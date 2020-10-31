def triplet(array,size):
    i = 2
    count = 0
    while i < size:
        end_index = i-1
        start_index = 0
        while(start_index<end_index):
            sum = array[start_index] + array[end_index]
            if sum == array[i]:
                count += 1
                start_index +=1
                end_index -=1
            elif sum < array[i]:
                start_index += 1
            elif sum > array[i]:
                end_index -=1
        i +=1
    if count == 0:
        return -1
    else:
        return count

t = int(input("enter the test cases: "))
for i in range(t):
    size = int(input("Enter the size: "))
    array = list(map(int, input("enter the array: ").strip().split()))
    print(triplet(array,size))
