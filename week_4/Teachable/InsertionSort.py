def insertionSort(arr):
    num_swaps = 0
    for i in range(1,len(arr)):
        for j in range(i,0,-1):
            if arr[j] < arr[j-1]:
                num_swaps += 1
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:
                break

    return num_swaps






if __name__ == '__main__':
    #best case
    arr1 = [1,2,3,4,10,6,7,8,9,5]
    #O(N) - runtime
    #O(1) - space
    print(insertionSort(arr1))
    print(arr1)

    #worst case
    #O(N^2)/2 -> O(N^2) - runtime
    #O(1) - space
    print("////////////////")
    arr2 = [10,9,8,7,6,5,4,3,2,1]
    print(insertionSort(arr2))
    print(arr2)
