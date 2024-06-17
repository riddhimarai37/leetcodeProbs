class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = {}

        for c in magazine:
            counter[c] = 1 + counter.get(c, 0)

        for c in ransomNote:
            if c in counter and counter[c] > 0:
                counter[c] -= 1
            else:
                return False

        return True
        