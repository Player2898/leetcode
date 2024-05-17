class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        maxi = max(score)
        # a list of size maxi is created with None values.
        index_ofScores = [None] * (maxi + 1) 
        ans = [None] * n
        index = 0

        #for each score value their index position is assigned as their value in index_ofScores.
        for i in score:
            index_ofScores[i] = index
            index += 1
        
        ranks = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        positions = 4

        #reversing index_ofScores to assign their positions in the game.
        for i in index_ofScores[::-1]:
            if i is not None:
                if len(ranks) != 0:
                    ans[i] = ranks[0]
                    ranks.pop(0)
                    #print(ans)
                else:
                    ans[i] = str(positions)
                    positions += 1
        return ans
