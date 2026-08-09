class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        
        for point in points:
            # Calculate distance squared (no need sqrt, monotonic)
            dist_sq = point[0]**2 + point[1]**2
            
            # If heap has less than k, always add
            if len(maxHeap) < k:
                heapq.heappush(maxHeap, (-dist_sq, point))
            # If point is closer than farthest in heap, replace it
            elif dist_sq < -maxHeap[0][0]:
                heapq.heapreplace(maxHeap, (-dist_sq, point))
        
        # Extract points from heap (ignore distances)
        return [point for _, point in maxHeap]