"""https://leetcode.com/problems/determine-if-two-strings-are-close/"""


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        unique1 = list(set(word1))
        unique2 = list(set(word2))
        if sorted(unique1) != sorted(unique2):
            return False
        count_unique1 = list(map(word1.count, unique1))
        count_unique2 = list(map(word2.count, unique2))
        count_unique1.sort()
        count_unique2.sort()
        return count_unique1 == count_unique2
