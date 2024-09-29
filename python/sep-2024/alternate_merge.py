class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p1, p2 = 0, 0
        list1 = list(word1)
        list2 = list(word2)
        out = []
        print(list1)
        print(list2)
        j = 0
        for i in range(0, len(list1)):
            out.append(list1[i])
            out.append(list2[j])
            j += 1
        print(i)
        if j > len(list1):
            for k in range(j, k):
                out.append(list2[j])
                j += 1
        if len(list1) < len(list2):
            out.append(list2[j])
        print(out)
    
Solution().mergeAlternately(word1="fir", word2="waterere")