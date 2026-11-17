class Solution:

    """
    clarifying question
    1. string is not null or empty 
    2. all the letters are upper case or mix bag 
    
    """

    """
    solution 1 - sort both the sting and compare 
    time O(nlogn+mlogm)
    space O(1) or O(n+m) based on sorting algo

    """
    def isAnagram2(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False

        return sorted(s) == sorted(t)

    """
    solution -2 with hashmap  add each char of a string in a diff hash and then 
    compare 2 hashmap
    
    time O(n+m)
    space O(1) 
    
    """
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {} # char -> occurance

        for i in range(len(s)):
            # here adding value to map char --> occurance 
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT






