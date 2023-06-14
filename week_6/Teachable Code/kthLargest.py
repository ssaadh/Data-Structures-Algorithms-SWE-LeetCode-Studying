import heapq

#import pq
#constructor(k) - initializes a min pq of size k
#add(val) - removes smallest element and adds value and reheapifies

#[3,2,1,5,6,4]
#[1,2,3,4,5,6]
#O(nlgn)

#pq - size k
#O(nlgk)

#[3,2,1,5,6,4]
#pq = [5,6]

#2n*lg(k) - nlg(k)
class Solution:
    def findKthLargest(self, nums, k):
        #initialize our pq with first k elements
        pq = []
        for i in range(k):
                heapq.heappush(pq, nums[i])

        #iterate through rest of elements

        for num in nums[k:]:
                if num > pq[0]:
                        #if element is greater than min element on PQ pop min element and add new element - reheapify
                        heapq.heappop(pq)
                        heapq.heappush(pq,num)

        #return smallest element
        return pq[0]
