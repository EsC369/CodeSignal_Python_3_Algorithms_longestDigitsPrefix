"""
Given a string, output its longest prefix which contains only digits.

Example

For inputString="123aa1", the output should be
longestDigitsPrefix(inputString) = "123".

"""

def longestDigitsPrefix(inputString):
    for i in range(len(inputString)):
        if not inputString[i].isdigit():
            return inputString[0:i]
    return inputString
