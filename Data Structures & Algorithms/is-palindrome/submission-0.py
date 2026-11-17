class Solution:
    """
    solution - 1 
    space O(n)
    time O(n)

    follow solution - 1 algorithm 


    """
    def isPalindrome1(self, s: str) -> bool:
        newStr = ""
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        """
        newStr[::-1] string[start:stop:step]. leaving start and stop blank 
        tell python to look entire string and then step through string backward
        one char at a time
        """        
        return newStr == newStr[::-1]
    """
    solution - 2 
    follow solution - 2 algorithm but implementation is different 
    time : O(n)
    space : O(1)

    """    

    def isPalindrome(self, s: str) -> bool:    

        l, r = 0, len(s) - 1

        while l < r:
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r -=1
                continue
            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1
            
        return True








