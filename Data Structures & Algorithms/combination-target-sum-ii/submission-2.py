class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtrack(subset, idx, count):
            if count==target:
                res.append(subset.copy())
                return
            if count>target or idx>=len(candidates):
                return
            
            #include
            count+=candidates[idx]
            subset.append(candidates[idx])
            backtrack(subset, idx+1, count)
            subset.pop()
            count-=candidates[idx]

            # we want to skip the duplicates because we don't want to process the same combinations and store them again in the result
            nxt_idx = idx+1
            while nxt_idx<len(candidates) and candidates[nxt_idx]==candidates[idx] :
                nxt_idx+=1
            backtrack(subset, nxt_idx, count)
        backtrack([], 0, 0)
        return res