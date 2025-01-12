class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        
        if len(s)%2==1:
            return False
        
        star=[]
        open_bracket=[]

        for i in range(len(s)):

            if locked[i]== '0':
                star.append(i)
            elif s[i] == '(':
                open_bracket.append(i)
            elif s[i] == ')':
                if open_bracket:
                    open_bracket.pop()
                elif star:
                    star.pop()
                else:
                    return False
        
        while open_bracket and star and open_bracket[-1] < star[-1] :
            open_bracket.pop()
            star.pop()

        if open_bracket:
            return False

        return True

                
