class Solution:
    def sortSentence(self, s: str) -> str:
        # 文章を分割する
        s = s.split()
        hashmap = {}
        
        # HashMapにキーとして数値、アイテムとして単語を格納
        for i in range(len(s)):
            hashmap[s[i][-1]] = s[i][:-1]
            
        # インデックス0から順番に値を格納し、連結させたものを返り値として返却する
        for key, value in hashmap.items():
            s[int(key) - 1] = value
        print(s)
        return " ".join(s)
# Runtime: 49 ms, faster than 28.49% of Python3 online submissions for Sorting the Sentence.
# Memory Usage: 13.9 MB, less than 86.17% of Python3 online submissions for Sorting the Sentence.

            
