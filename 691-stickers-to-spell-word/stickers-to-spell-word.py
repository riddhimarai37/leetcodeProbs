class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        sticker_counts = [collections.Counter(sticker) for sticker in stickers]
        memo = {}

        def dfs(target_str):
            if not target_str:
                return 0

            if target_str in memo:
                return memo[target_str]

            target_counter = collections.Counter(target_str)

            ans = float('inf')

            for sticker in sticker_counts:
                if target_str[0] not in sticker:
                    continue

                rem_chars = target_counter - sticker

                letters = [char * count for char,count in rem_chars.items()]

                next_target = "".join(letters)

                ans = min(ans, 1 + dfs(next_target))
                    
            memo[target_str] = ans
            return ans

        ans = dfs(target)

        if ans == float('inf'):
            return -1

        return ans

        