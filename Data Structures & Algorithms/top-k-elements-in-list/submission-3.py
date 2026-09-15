class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = (defaultdict(int))
        for i in nums:
            freq[i] +=1

        nlis = sorted(freq.items(), key = lambda x: x[1], reverse = True)
        nlis1 = (num for num, val in nlis)
        return(list(nlis1)[:k])


        
