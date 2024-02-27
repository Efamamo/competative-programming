class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        if len(deck)==1:
            return deck
        queue = deque()
        deck.sort()
        queue.append(deck[-1])
        queue.append(deck[-2])

        for i in range(len(deck)-3,-1,-1):
            queue.append(queue.popleft())
            queue.append(deck[i])
        queue.reverse()
        return queue
    
        