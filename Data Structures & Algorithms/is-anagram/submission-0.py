class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        hashA = {}
        hashB = {}

        for stringA in s:
            if stringA not in hashA:
                hashA[stringA] = 1
            else:
                hashA[stringA] +=1 

        for stringB in t:
            if stringB not in hashB:
                hashB[stringB]= 1
            else:
                hashB[stringB] +=1 
        
        if len(s) != len(t):
            return False 
        else:
           
            return  hashA == hashB 

    