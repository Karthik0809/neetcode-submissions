class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        prefix_map = { 0: 1}
        result = 0
        for num in nums:
            prefix_sum += num
            complement  = prefix_sum - k
            if complement in prefix_map:
                result += prefix_map[complement]

            prefix_map[prefix_sum] = prefix_map.get(prefix_sum, 0) + 1
        return result



        