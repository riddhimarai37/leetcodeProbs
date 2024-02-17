

class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        word_ptr = abbr_ptr = 0

        while word_ptr < len(word) and abbr_ptr < len(abbr):
            if abbr[abbr_ptr].isdigit():
                if abbr[abbr_ptr] == "0":
                    return False
                num = 0
                while abbr_ptr < len(abbr) and abbr[abbr_ptr].isdigit():
                    num = num * 10 + int(abbr[abbr_ptr])
                    abbr_ptr += 1
                word_ptr += num
            else:
                if abbr[abbr_ptr] != word[word_ptr]:
                    return False
                abbr_ptr += 1
                word_ptr += 1

        return word_ptr == len(word) and abbr_ptr == len(abbr)




























        # pt1 = pt2 = 0

        # while pt1 < len(word) and pt2 < len(abbr):
        #     if abbr[pt2].isdigit():
        #         if abbr[pt2] == '0':
        #                 return False
        #         number_str = ""
        #         while pt2 < len(abbr) and abbr[pt2].isdigit():
        #             number_str += abbr[pt2]
        #             pt2 += 1

        #         num = int(number_str)

        #         pt1 += num
        #     else:
        #         if abbr[pt2] != word[pt1]:
        #             return False
        #         pt1 += 1
        #         pt2 += 1

        # return pt1 == len(word) and pt2 == len(abbr)


        # abbr_pt = word_pt = 0

        # while word_pt < len(word) and abbr_pt < len(abbr):
        #     if abbr[abbr_pt].isdigit():
        #         steps = 0
        #         # leading zero 
        #         if abbr[abbr_pt] == '0':
        #             return False
        #         while abbr_pt < len(abbr) and abbr[abbr_pt].isdigit():
        #             steps = steps * 10 + int(abbr[abbr_pt])
        #             abbr_pt += 1
        #         word_pt += steps
        #     else:
        #         if abbr[abbr_pt] != word[word_pt]: 
        #             return False

        #         abbr_pt += 1
        #         word_pt += 1

        # return abbr_pt == len(abbr) and word_pt == len(word)

        # # Time = O(N)
        # # Space = O(1)





            



            











