class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Convert to max heap by negating all values
        maxHeap = [-stone for stone in stones]
        heapq.heapify(maxHeap)
        
        # Keep smashing until 1 or 0 stones remain
        while len(maxHeap) > 1:
            # Extract two heaviest stones (most negative = largest)
            first = -heapq.heappop(maxHeap)   # Negate back to positive
            second = -heapq.heappop(maxHeap)  # Negate back to positive
            
            # If they're not equal, push the difference back
            if first != second:
                heapq.heappush(maxHeap, -(first - second))
            # If equal, both destroyed (don't push anything)
        
        # Return last stone or 0 if none remain
        return -maxHeap[0] if maxHeap else 0
        