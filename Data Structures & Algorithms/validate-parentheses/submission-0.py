class Solution:
    def isValid(self, s: str) -> bool:
        bstack = list()
        track_brackets = {
            '[' : ']',
            '{' : '}',
            '(' : ')'
        }
        for b in s:
            if b in track_brackets:
                bstack.append(b)
            else:
                if bstack and track_brackets[bstack[-1]] == b:
                    bstack.pop()
                else:
                    return False
        return not bstack
        