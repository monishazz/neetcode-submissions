class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_list = []
        for word in strs:
            encode_list.append(str(len(word)))
            encode_list.append('<')
            encode_list.append(word)
        return "".join(encode_list)



    def decode(self, s: str) -> List[str]:
        decode_list = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '<':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            decode_list.append(s[i:j])
            i = j

        return decode_list
