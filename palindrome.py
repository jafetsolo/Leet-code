class Solution(object):
    def isPalindrome(self, x):
        c = str(x)
        reversed_string = c[::-1]

        if reversed_string == c:
            return True
        return False

        """
        :type x: int
        :rtype: bool
        """
