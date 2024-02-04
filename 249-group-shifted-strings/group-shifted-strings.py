# for strings to be in the same seq: 1. same length 2. subtract the ord(c) from e/o, if theyre the same then part of the sequence
# first group the strings by length
# 

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        seq_map = collections.defaultdict(list)
        
        for string in strings:
            # edge case 
            if len(string) == 1:
                seq_map[(-1,)].append(string)
            else:
                char_diffs = []
                i = 1
                
                while i < len(string):
                    char_diffs.append((ord(string[i]) - ord(string[i-1])) % 26)
                    i += 1
                    
                # key --> list of words with that sequence
                seq_map[tuple(char_diffs)].append(string)
            
        return seq_map.values()

        # Time O(N * k); n= number of strings given, k is the length of each string
        # Space: O(N * K)
