class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # step 1: get the frequency count
        freq = {}
        for num in nums:
            freq[num] = freq.get(num,0)+1
        #step 2: create a min heap, if the size increases then k remove the top(that's the minimum element. All the other elements are within k)
        
        min_heap = []
        for number, frequency in freq.items():
            heapq.heappush(min_heap, (frequency, number))

            if(len(min_heap)>k):
                heapq.heappop(min_heap)
        
        return [number for frequency,number in min_heap]
