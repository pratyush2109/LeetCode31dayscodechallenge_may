class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
         answer = []
         m, n = len(s), len(p)
         if m < n:
            return answer
         pCounter = Counter(p)
         sCounter = Counter(s[:n-1])

         i = 0
         for i in range(n - 1, m):
            sCounter[s[i]] += 1
            if sCounter == pCounter:
                answer.append(i - n + 1)
            sCounter[s[i - n + 1]] -= 1
            if sCounter[s[i - n + 1]] == 0:
                del sCounter[s[i - n + 1]]
         return answer
                