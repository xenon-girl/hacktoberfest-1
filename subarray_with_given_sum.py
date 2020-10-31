t = int(input("enter the test cases: "))

for i in range(t):
    # size, sub_sum= int(input("Enter the size: "))
    size, sub_sum =list(map(int, input("enter the size of array and sum of the subarray: ").strip().split()))
    # sub_sum = int(input("enter the sum of the subarray :"))
    array = list(map(int, input("enter the array: ").strip().split()))
    currsum = 0
    start_index = 0
    end_index = size-1
    for i in range(size):

        if currsum < sub_sum:
            end_index = i
            currsum += array[i]
        while(currsum > sub_sum):
            currsum -= array[start_index]
            start_index += 1

        if currsum == sub_sum:
            print(start_index+1,end_index+1)
            break

    if currsum != sub_sum:
        print(-1)


