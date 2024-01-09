class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        str_pt = 0
        abbr_pt = 0

        while str_pt < len(word) and abbr_pt < len(abbr):
            if abbr[abbr_pt].isdigit():
                # leading zero
                if abbr[abbr_pt] == '0': return False
                shift = 0
                while abbr_pt < len(abbr) and abbr[abbr_pt].isdigit():
                    shift = (shift*10) + int(abbr[abbr_pt])
                    abbr_pt += 1
                str_pt += shift
            else:
                if word[str_pt] != abbr[abbr_pt]: return False
                str_pt += 1
                abbr_pt += 1

        return str_pt == len(word) and abbr_pt == len(abbr)







        