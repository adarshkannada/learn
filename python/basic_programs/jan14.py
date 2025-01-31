from collections import deque
from collections import Counter
class Solution:
    

    def isValid(self, s: str) -> bool:
        stack = deque(s)
        print(stack)
        if len(stack) % 2 == 0:
            i = len(stack) - 1
            for each in stack:
                if stack.pop() == s[i]:
                    i-=1
                else:
                    print("smoke")
        else:
            print("smoke")


    def count_words(self,s: str) -> dict:
        counted = Counter(s.split())
        print(counted)

    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        for i in range(0, len(s)-1):
            if s[i] != s[i+1]:
                max_length += 1
        print(max_length)

    def mergeAlternately(self, word1: str, word2: str) -> str:
        """merge string values alternatively """
        result = []
        for w1, w2 in zip(word1, word2):
            result.append(w1+w2)
        result.append(word1[len(word2):]) # append remaining values from word2 to result list
        result.append(word2[len(word1):]) # append remaining values from word1 to result list
        print(result)
        print("".join(result))

# Solution().isValid(s="{}[]{}()")
# Solution().count_words(s="this this is is is is is here now!")
# Solution().lengthOfLongestSubstring(s="firee")
Solution().mergeAlternately(word1="sas", word2="free")