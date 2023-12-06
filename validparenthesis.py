class Solution(object):
    def isValid(self, s):
        # Initialize a stack
        stack = []

        # Mapping of closing brackets to their corresponding opening brackets
        bracket_map = {")": "(", "}": "{", "]": "["}

        # Iterate through the string
        for char in s:
            # If the character is a closing bracket
            if char in bracket_map:
                # Pop from the stack or use a dummy character if the stack is empty
                top_element = stack.pop() if stack else '#'

                # Check if the popped element matches the corresponding opening bracket
                if bracket_map[char] != top_element:
                    return False
            else:
                # Push opening brackets onto the stack
                stack.append(char)

        # If the stack is empty, all brackets were matched correctly
        return not stack
        """
        :type s: str
        :rtype: bool
        """
