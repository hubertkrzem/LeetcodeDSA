class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return chr(20)

        output = []
        for word in strs:
            curr_word = []
            for char in word:
                curr_word.append(chr(ord(char) + 1))

            output.append("".join(curr_word))

        return " ".join(output)

    def decode(self, s: str) -> List[str]:
        if s == chr(20):
            return []

        s = s.split(" ")
        
        output = []
        for word in s:
            curr_word = []
            for char in word:
                curr_word.append(chr(ord(char) - 1))

            output.append("".join(curr_word))

        string_out = " ".join(output)

        return output