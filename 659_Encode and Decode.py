class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        newStr = ""
        for i in strs:
            newStr += i
            newStr += ":13y8:6317:8391:"
        return newStr

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str2):
        # write your code here
        str2 = str(str2)
        return str2.split(":13y8:6317:8391:")[:-1]