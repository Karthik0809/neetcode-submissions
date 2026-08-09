class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k  # Store the position we're tracking
        self.heap = nums  # Use input array as the heap
        heapq.heapify(self.heap)  # Convert to min heap in O(n)
        
        # Keep only k largest elements by removing smallest ones
        while len(self.heap) > k:
            heapq.heappop(self.heap)  # Remove minimum element

    def add(self, val: int) -> int:
        # If heap has less than k elements, always add new value
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        # If new value is larger than minimum (kth largest), replace it
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap, val)  # Pop min, push new val
        
        # Root of min heap is always the kth largest element
        return self.heap[0]
    
        
