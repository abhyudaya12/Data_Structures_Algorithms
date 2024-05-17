# See the commented code:

#from queue import PriorityQueue
class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        # arr = []
        # pq = PriorityQueue()
        # for items in nums:
        #     pq.put(items)
        
        # while not pq.empty():
        #     alice = pq.get()
        #     bob = pq.get()
        #     arr.append(bob)
        #     arr.append(alice)
        # return arr
        nums.sort()
        i=0
        while(i<len(nums)):
            nums[i],nums[i+1]=nums[i+1],nums[i]
            i+=2
        return nums
