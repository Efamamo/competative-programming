class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        size = len(cardPoints) - k
        minSubArraySum = float('inf')
        l = curr = 0
        
        for r, v in enumerate(cardPoints):
            curr += v
            if r - l + 1 > size:
                curr -= cardPoints[l]
                l += 1
            if r - l + 1 == size:    
                minSubArraySum = min(minSubArraySum, curr)
				
        return sum(cardPoints) - minSubArraySum