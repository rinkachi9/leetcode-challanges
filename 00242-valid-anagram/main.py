class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dictionary = {}

        for index in range(len(s)):
            dictionary[s[index]] = dictionary.get(s[index], 0) + 1
            dictionary[t[index]] = dictionary.get(t[index], 0) - 1

        for letter in dictionary:
            if dictionary[letter] != 0:
                return False

        return True


solution = Solution()
print(solution.isAnagram("anagram", "nagar"))
print(solution.isAnagram("rat", "car"))
