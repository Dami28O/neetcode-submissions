class Solution:

    def encode(self, strs: List[str]) -> str:
        # use string length and # followed by str len
        arr = []

        for s in strs:
            length = len(s)
            arr.append(str(length))
            arr.append("#")
            arr.append(s)
        
        # combine into single string
        encoded = "".join(arr)

        return encoded

    def decode(self, s: str) -> List[str]:
        
        # based on the # len pattern
        arr = []
        subarr = []
        strlen = []

        i = 0
        while i < len(s):

            # only should run into val determining str length 
            # and the end of code

            if s[i] != "#":
                strlen.append(s[i])
                i += 1
            else:
                # met end of delimiter
                tmp = "".join(strlen)
                extend = int(tmp)
                strlen.clear()
                # reset str length counter
                subarr = s[i + 1: i + extend + 1]
                substr = "".join(subarr)
                arr.append(substr)
                subarr = []
                # extend the str counter forward
                i += extend + 1
        return arr
            

