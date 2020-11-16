class Solution:
    def romanToInt(self, s: str) -> int:
        alphabets = {'I': 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        res = 0
        prev = ""
        for char in s:
            res += alphabets[char]
            if prev != "" and (alphabets[prev] < alphabets[char]):
                res -= 2*alphabets[prev]
            prev = char
        return res