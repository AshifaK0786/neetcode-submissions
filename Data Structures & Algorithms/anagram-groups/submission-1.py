class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for ch in strs:
            k="".join(sorted(ch))
            if k not in d:
                d[k]=[]
            d[k].append(ch)
        return list(d.values())