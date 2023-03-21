# Topic : BASIC PYTHON
#Exercise Number : 6
##PROBLEM STATEMENT:
#   Read input string from user. Your task is to 
#   find out if the string  contains: alphanumeric characters, alphabetical characters, 
#   digits, lowercase and uppercase characters.

# Python Version : 3.7

"""
    Input Format
        A single line containing a string .
    Output Format
    In the first line, print True if  has any alphanumeric characters. Otherwise, print False.
    In the second line, print True if  has any alphabetical characters. Otherwise, print False.
    In the third line, print True if  has any digits. Otherwise, print False.
    In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
    In the fifth line, print True if  has any uppercase characters. Otherwise, print False.
    Sample Input
        qA2
    Sample Output
        True
        True
        True
        True
        True
"""

def alphanumeric(s):
    for i in range(len(s)):
        if(s[i].isalnum()):
            return True;
    return False;
        
def alphabetical(s):
    for i in range(len(s)):
        if(s[i].isalpha()):
            return True;
    return False;

def digits(s):
    for i in range(len(s)):
        if(s[i].isdigit()):
            return True;
    return False;

def lowercase(s):
    for i in range(len(s)):
        if(s[i].islower()):
            return True;
    return False; 
     
def uppercase(s):
    for i in range(len(s)):
        if(s[i].isupper()):
            return True;
    return False;

s = "qA2"

print(alphanumeric(s))
print(alphabetical(s))
print(digits(s))
print(lowercase(s))
print(uppercase(s))

