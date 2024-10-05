class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        out = []
        # Looping through both words until end is reached
        while i < len(word1) and j < len(word2):
            out.append(word1[i])
            out.append(word2[j])
            i += 1
            j += 1

        # adding remaining characters of word1 or word2 if any
        if i < len(word1):
            out.append(word1[i:])
        if j < len(word2):
            out.append(word2[j:])

        out_str = ''.join(out)
        print(out_str)
        return out_str

    
Solution().mergeAlternately(word1="fir", word2="waterere")
