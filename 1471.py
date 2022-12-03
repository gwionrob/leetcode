"""https://leetcode.com/problems/the-k-strongest-values-in-an-array/"""


class Solution:
    def getStrongest(self, arr: list[int], k: int) -> list[int]:
        if len(set(arr)) <= 1:
            return [arr[0]] * k
        arr.sort()
        middle_index = len(arr) - 1 // 2
        median = arr[middle_index]
        strength = []
        for i in arr:
            strength.append(abs(i - median))
        strength_dict: dict = {}
        for key in arr:
            for value in strength:
                if key in strength_dict:
                    strength_dict[key] = (
                        strength_dict[key]
                        if isinstance(strength_dict[key], list)
                        else [strength_dict[key]]
                    ) + [value]
                else:
                    strength_dict[key] = value
                strength.remove(value)
                break
        sorted_val_strength_dict = dict(
            sorted(
                strength_dict.items(),
                reverse=True,
                key=lambda item: (
                    item[1] if isinstance(item[1], int) else item[1][0],
                    item[0],
                ),
            )
        )
        keys = list(sorted_val_strength_dict.keys())[:k]
        interested_dict = {k: sorted_val_strength_dict[k] for k in keys}
        strongest: list = []
        for key in interested_dict:
            if len(strongest) < k:
                if isinstance(interested_dict[key], list):
                    for i in interested_dict[key]:
                        strongest.append(key)
                else:
                    strongest.append(key)
        return strongest[:k]
