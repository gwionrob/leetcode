"""https://leetcode.com/problems/sort-characters-by-frequency/"""


class Solution:
    def frequencySort(self, s: str) -> str:
        unique_char = list(set(s))
        char_count = dict(zip(unique_char, list(map(s.count, unique_char))))
        sorted_count = dict(
            sorted(char_count.items(), reverse=True, key=lambda item: item[1])
        )
        return_str = ""
        for key in sorted_count:
            return_str = return_str + key * sorted_count[key]
        return return_str
