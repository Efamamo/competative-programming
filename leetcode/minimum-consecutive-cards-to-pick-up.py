class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        counter = {}
        l=0
        minimum = len(cards) + 1
        for r in range(len(cards)):
            while cards[r] in counter:
                minimum = min(minimum,r-l+1)
                counter[cards[l]]-=1
                if counter[cards[l]] == 0:
                    del counter[cards[l]]
                l+=1
            
            counter[cards[r]] = counter.get(cards[r],0)+1
            
        return minimum if minimum!=len(cards)+1 else -1
        