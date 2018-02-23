class Solution:
    """
    @param: string: An array of Char
    @param: length: The true length of the string
    @return: The true length of new string
    """
    def replaceBlank(self, string, length):
        if string is None or length == 0:
            return length
        cnt = 0
        for s in string:
            if s == ' ':
                cnt += 1
        l = length + 2 * cnt
        j = l - 1
        for i in range(length-1, -1, -1):
            if string[i] == ' ':
                string[j] = '0'
                string[j-1] = '2'
                string[j-2] = '%'
                j -= 3
            else:
                string[j] = string[i]
                j -= 1
        return l