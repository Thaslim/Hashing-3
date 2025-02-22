"""
TC: O(n)
SP: O(n)
use rolling hash technique to avoid creating new substring in the sliding window
"""
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        nucleotides_map = {"A": 1, "C": 2, "G": 3, "T": 4}
        l = i = 0
        all_seq = set()
        res = set()
        rolling_hash = 0
        while i < len(s):
            rolling_hash = rolling_hash * 4 + nucleotides_map[s[i]] + 1
            if i - l + 1 == 10:
                if rolling_hash in all_seq:
                    res.add(s[l : i + 1])
                else:
                    all_seq.add(rolling_hash)
                rolling_hash = rolling_hash - (nucleotides_map[s[l]] + 1) * pow(4, 9)
                l += 1
            i += 1
        return list(res)
