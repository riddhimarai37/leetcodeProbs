

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        dic = collections.defaultdict(list)

        for idx, s in enumerate(strings):
            if len(dic) == 0:
                dic[s].append(s)
                continue
            
            equal = True

            for key in dic.keys():
                print(key, s)
                if len(key) == len(s):
                    equal = True
                    diff = (ord(key[0]) - ord(s[0])) % 26
                    i = 1
                    while i < len(s):
                        if (ord(key[i]) - ord(s[i])) % 26 != diff:
                            equal = False
                            break
                        i += 1
                    if equal:
                        dic[key].append(s)
                        break
                else:
                    equal = False
            
            if not equal:
                dic[s].append(s)

        return list(dic.values())


                    
                    
                        
                    



                        

            




















        # seq_map = collections.defaultdict(list)
        
        # for string in strings:
        #     # edge case 
        #     if len(string) == 1:
        #         seq_map[(-1,)].append(string)
        #     else:
        #         char_diffs = []
        #         i = 1
                
        #         while i < len(string):
        #             char_diffs.append((ord(string[i]) - ord(string[i-1])) % 26)
        #             i += 1
                    
        #         # key --> list of words with that sequence
        #         seq_map[tuple(char_diffs)].append(string)
            
        # return seq_map.values()

        # Time O(N * k); n= number of strings given, k is the length of each string
        # Space: O(N * K)
