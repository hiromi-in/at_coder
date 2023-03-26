"""
Problem Statement
You are given a string 
S. Each character of 
S is uppercase or lowercase English letter. Determine if 
S satisfies all of the following conditions:

The initial character of 
S is an uppercase A.
There is exactly one occurrence of C between the third character from the beginning and the second to last character (inclusive).
All letters except the A and C mentioned above are lowercase.
Constraints
4≤∣S∣≤10 (
∣S∣ is the length of the string 
S.)
Each character of 
S is uppercase or lowercase English letter.
"""

def checkAC(s):
    if not s[0] == "A":
      return False

    if s[2:-1].count("C") != 1:
      return False

    if sum(map(str.isupper, s)) != 2:
      return False
  
    return True

print("AC" if checkAC(input()) else "WA")
