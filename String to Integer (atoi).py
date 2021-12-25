class Solution:
    def myAtoi(self, s: str) -> int:
        # 空白削除のためのstrip関数
        s = s.strip()
        # 長さが0(=何もない)、長さが0より大きいが、最初の文字に+ないしは-がない時、数字でない時、空白文字の場合は0を返す
        if len == 0 or (len(s) > 0 and not (s[0] in ["+","-"] or s[0].isdigit())) or s == "":
            return 0
        value = 0
        # signは先頭文字が-である時に-1、+のときは1を返す。後でvalueの値にかけることで符号を管理する
        sign = -1 if s[0] == '-' else 1
        # 先頭文字が数字ではなかった場合(符号)には添字"i"を1から始めることで2文字目からスタートする
        i = 1 if not s[0].isdigit() else 0
        # iがsの最後の添字までたどり着くか数字に変換不能な文字が来るまでループ
        while i < len(s) and s[i].isdigit():
            # valueを桁上げしていくことで数字の桁がスライドされる。
            # ord関数は文字列をUnicodeに変える。ここの例ならば"4"→52、"0"→48で前者から後者を引いた値を1の位に入れ、既存のvalueの値は桁上げを繰り返す
            value = (value*10) + (ord(s[i]) - ord("0"))
            i += 1
        value *= sign
        # もし値が2**31乗を超える値、もしくは-(2**31)乗を下回る値だった場合には以下の値を返す
        if value < -(2**31):
            return -(2**31)
        elif value > (2**31) -1:
            return (2**31) -1
        return value
# Runtime: 28 ms, faster than 94.56% of Python3 online submissions for String to Integer (atoi).
# Memory Usage: 14.2 MB, less than 57.60% of Python3 online submissions for String to Integer (atoi).
