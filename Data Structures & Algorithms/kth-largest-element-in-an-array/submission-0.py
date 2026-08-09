class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minheap = nums[:]
        heapq.heapify(minheap)  # Modifies in-place, returns None
        
        # Keep only k elements (k largest)
        while len(minheap) > k:  # Compare LENGTH, not heap itself
            heapq.heappop(minheap)
        
        # Return the root (kth largest)
        return minheap[0]
        