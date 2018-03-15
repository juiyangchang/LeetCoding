class Solution:
    cache = {}
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if (s, p) in self.cache:
            return self.cache[(s, p)]
        
        if p == '':
            return s == ''
        
        if p[-1] == '*':
            if self.isMatch(s, p[:-2]):
                self.cache[(s, p)] = True
                return True
            if s and len(p) > 1 and p[-2] in ('.', s[-1]) and self.isMatch(s[:-1], p):
                self.cache[(s, p)] = True
                return True
            
        if s and p[-1] in ('.', s[-1]) and self.isMatch(s[:-1], p[:-1]):
            self.cache[(s, p)] = True
            return True
        
        self.cache[(s, p)] = False
        return False   