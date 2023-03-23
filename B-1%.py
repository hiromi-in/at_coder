"""
Problem Statement
Takahashi has a deposit of 
100 yen (the currency of Japan) in AtCoder Bank.

The bank pays an annual interest rate of 
1 % compounded annually. (A fraction of less than one yen is discarded.)

Assuming that nothing other than the interest affects Takahashi's balance, in how many years does the balance reach 
X yen or above for the first time?

Constraints
101≤X≤10 
18
 
All values in input are integers.
"""

x = int(input())
original = 100
year = 0

while original < x:
  year += 1
  original = original + original//100

print(year)
