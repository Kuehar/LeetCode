class Solution:
    def groupThePeople(self, groupSizes):
        ans,group,next_group = [],[],[]
        for i,j in enumerate(groupSizes):
            group.append((j,i))
        group.sort()
        for length,index in group:
            next_group.append(index)
            if len(next_group) == length:
                ans.append(next_group)
                next_group = []    
        return ans
# Runtime: 64 ms, faster than 75.60% of Python online submissions for Group the People Given the Group Size They Belong To.
# Memory Usage: 12.7 MB, less than 59.40% of Python online submissions for Group the People Given the Group Size They Belong To.
