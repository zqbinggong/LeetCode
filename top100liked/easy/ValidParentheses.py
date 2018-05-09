class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        if n == 0:
            return True
        if n % 2 != 0:
            return False
        #如此循环是因为括号之间会存在嵌套
        while '()' in s or '[]' in s or '{}' in s:
            s = s.replace('()', '').replace('[]', '').replace('{}', '')
        if s == '':
            return True
        else:
            return False


