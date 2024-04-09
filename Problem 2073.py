class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        x = tickets[k]
        result = 0
        for i in range(len(tickets)):
            if i <= k :    #people standing before k buys atmost x tickets
                tickets[i] = x  if tickets[i] >= x else tickets[i] 
                
            else:          #people behind k buys atmost x-1 tickets
                tickets[i] = x-1  if tickets[i] >= x else tickets[i]
    
            result += tickets[i]
        return result
