#tar: 15
#                 lo      mid      hi
#[13,15,17,19,-5,-3,-1,0,1,3,5,7,9,11]
           #lo    mid              hi
#[-5,-3,-1,0,1,3,5,7,9,11,-100,-50,-30]


#assume no duplicates in array
def searchRotatedArray(arr, target):
    #runtime - O(lgN)
    #space - O(1)
    lo = 0
    hi = len(arr) - 1
    while(lo <= hi):
        mid = (lo + hi)//2
        #if we find the element then we are done
        if arr[mid] == target:
            return mid
        #case 1 arr[lo] > arr[mid] -> we have pivot in between
        if arr[lo] > arr[mid]:
            if target >= arr[lo] or target <= arr[mid]:
                hi = mid - 1
            else:
                lo = mid + 1

        #pivot is not within arr[lo] - arr[mid]
        else:
            #case 2 arr[lo] < arr[mid] -> no pivot, so if target is within arr[lo] and arr[mid]
            #then we just perform normal binary search
            #if target is not within arr[lo] <= target < arr[mid] then if it exists its in upper half
            if arr[lo] <= target < arr[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
    return -1


def searchRotatedArrayWithDuplicates(arr, target):
    #runtime - O(N)
    #average runtime - O(lgN)
    #space - O(1)
    lo = 0
    hi = len(arr) - 1
    while(lo <= hi):
        mid = (lo + hi)//2
        #if we find the element then we are done
        if arr[mid] == target:
            return mid

        while(lo != mid and arr[mid] == arr[lo]):
            lo += 1
        #case 1 arr[lo] > arr[mid] -> we have pivot in between
        if arr[lo] > arr[mid]:
            if target >= arr[lo] or target <= arr[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:
            if arr[lo] <= target < arr[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
    return -1



if __name__ == '__main__':
    #test cases
    arr = [1,3,5,7,9,11,13,15,17,19,21,23]
    rot_arr = [13,15,17,19,21,23,1,3,5,7,9,11]

    for i in range(0,24):
        print(i, ":",searchRotatedArray(arr,i), "|", searchRotatedArray(rot_arr, i))


    dup_arr = [-1,-1,1,1,1,2,2,2,4,4,4,5,5]
    target = 1

    print(searchRotatedArrayWithDuplicates(dup_arr,target))
