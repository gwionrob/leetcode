class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        first_half = s[: int(len(s) / 2)]
        second_half = s[int(len(s) / 2) :]
        print(first_half, second_half)
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        first_count = 0
        second_count = 0
        for vowel in vowels:
            if vowel in first_half:
                first_count += first_half.count(vowel)
            if vowel in second_half:
                second_count += second_half.count(vowel)
        print(first_count, second_count)
        return first_count == second_count
