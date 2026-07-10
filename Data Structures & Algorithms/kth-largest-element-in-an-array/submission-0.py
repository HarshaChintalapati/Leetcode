class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums1=[-s for s in nums]
        heapq.heapify(nums1)
        while(k>0):
            digit=heapq.heappop(nums1)
            k=k-1
        return -1 * digit

        