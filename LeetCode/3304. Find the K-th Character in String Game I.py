class Solution:
    def kthCharacter(self, k: int) -> str:
        def next_char(ch):
            return 'a' if ch == 'z' else chr(ord(ch) + 1)

        word = "a"
        while len(word) < k:
            next_part = ''.join(next_char(ch) for ch in word)
            word += next_part
        return word[k - 1]
