class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        prefix_map = {0 : 1}
        result = 0
        for num in nums:
            prefix_sum += num

            remainder = prefix_sum % k

            if remainder in prefix_map:
                result += prefix_map[remainder]

            prefix_map[remainder] =  prefix_map.get(remainder, 0) + 1

        return result 