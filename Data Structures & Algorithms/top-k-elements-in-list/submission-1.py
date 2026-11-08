class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = Counter(nums)
        heap = []
        for num, freq in freqMap.items(): 
            heapq.heappush(heap, (freq, num))
        
        for i in range(len(freqMap) - k): 
            heapq.heappop(heap)
        
        res = []
        for freq, num in heap: 
            res.append(num)
        return res
