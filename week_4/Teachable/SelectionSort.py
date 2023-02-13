def SelectionSort(arr):
    #O(N^2) time complexity. Space - O()
    for i in range(len(arr)): #O(N)
        min_number = arr[i]
        swap_index = i
        for j in range(i+1,len(arr)): #N-1, N-2 ... 1 -> O(N)
            if arr[j] < min_number:
                min_number = arr[j]
                swap_index = j

        arr[i], arr[swap_index] = arr[swap_index], arr[i]



if __name__ == '__main__':
    #test cases
    arr = [10,6,8,4,5,1,3,7,9,2]

    SelectionSort(arr)
    print(arr)
