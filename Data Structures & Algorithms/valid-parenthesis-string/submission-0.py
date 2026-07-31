class Solution:
    def checkValidString(self, s: str) -> bool:
        h=0
        l=0
        for ch in s:
            if ch=='(':
                h+=1
                l+=1
            elif ch==')':
                h-=1
                l-=1
            else:
                h+=1
                l-=1
            if h<0:
                return False
            l=max(l,0)
        return l==0