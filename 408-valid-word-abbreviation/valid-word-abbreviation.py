class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        abbr_pt = word_pt = 0

        while word_pt < len(word) and abbr_pt < len(abbr):
            if abbr[abbr_pt].isdigit():
                steps = 0
                # leading zero 
                if abbr[abbr_pt] == '0':
                    return False
                while abbr_pt < len(abbr) and abbr[abbr_pt].isdigit():
                    steps = steps * 10 + int(abbr[abbr_pt])
                    abbr_pt += 1
                word_pt += steps
            else:
                if abbr[abbr_pt] != word[word_pt]: 
                    return False

                abbr_pt += 1
                word_pt += 1

        return abbr_pt == len(abbr) and word_pt == len(word)


            



            















        
        # str_pt = 0
        # abbr_pt = 0

        # while str_pt < len(word) and abbr_pt < len(abbr):
        #     if abbr[abbr_pt].isdigit():
        #         # leading zero
        #         if abbr[abbr_pt] == '0': return False
        #         shift = 0
        #         while abbr_pt < len(abbr) and abbr[abbr_pt].isdigit():
        #             shift = (shift*10) + int(abbr[abbr_pt])
        #             abbr_pt += 1
        #         str_pt += shift
        #     else:
        #         if word[str_pt] != abbr[abbr_pt]: return False
        #         str_pt += 1
        #         abbr_pt += 1

        # return str_pt == len(word) and abbr_pt == len(abbr)







        