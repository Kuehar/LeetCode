class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first = ["q","w","e","r","t","y","u","i","o","p"]
        second = ["a","s","d","f","g","h","j","k","l"]
        third = ["z","x","c","v","b","n","m"]
        ans = []
        for word in words:
            first_count = second_count = third_count = 0
            for letter in word:
                if letter.lower() in first:
                    first_count = first_count + 1
                elif letter.lower() in second:
                    second_count = second_count + 1
                else:
                    third_count = third_count + 1
            if len(word) == first_count or len(word) == second_count or len(word) == third_count:
                ans.append(word)
        return ans
# Runtime: 28 ms, faster than 71.95% of Python3 online submissions for Keyboard Row.
# Memory Usage: 14.4 MB, less than 5.49% of Python3 online submissions for Keyboard Row.
