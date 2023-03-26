"""
Problem Statement
You have 
A 
500-yen coins, 
B 
100-yen coins and 
C 
50-yen coins (yen is the currency of Japan). In how many ways can we select some of these coins so that they are 
X yen in total?

Coins of the same kind cannot be distinguished. Two ways to select coins are distinguished when, for some kind of coin, the numbers of that coin are different.

Constraints
0≤A,B,C≤50
A+B+C≥1
50≤X≤20 
000
A, 
B and 
C are integers.
X is a multiple of 
50.
"""

a=int(input())
b=int(input())
c=int(input())
x=int(input())
count = 0

for num_500 in range(a+1):
  for num_100 in range(b+1):
    for num_50 in range(c+1):
      if num_50 * 50 + num_100 * 100 + num_500 * 500 == x:
        count += 1

print(count)
