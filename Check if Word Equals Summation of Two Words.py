class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        dic = {'a': '0', 'b': '1', 'c': '2', 'd': '3', 'e': '4', 'f': '5', 'g': '6', 'h': '7', 'i': '8', 'j': '9'}
        s1 = ''.join([dic[i] for i in firstWord])
        s2 = ''.join([dic[i] for i in secondWord])
        s3 = ''.join([dic[i] for i in targetWord])
        return (int(s1)+int(s2)) == int(s3)
# Runtime: 32 ms, faster than 75.04% of Python3 online submissions for Check if Word Equals Summation of Two Words.
# Memory Usage: 14.3 MB, less than 57.83% of Python3 online submissions for Check if Word Equals Summation of Two Words.
