"""
Problem Statement
Takahashi the Jumbo will practice golf.

His objective is to get a carry distance that is a multiple of 
K, while he can only make a carry distance of between 
A and 
B (inclusive).

If he can achieve the objective, print OK; if he cannot, print NG.

Constraints
All values in input are integers.
1≤A≤B≤1000
1≤K≤1000
"""

k = int(input())
a, b = map(int,input().split())
test = 0
 
for num in range(a,b+1):
  if num % k == 0:
    print("OK")
    test = 1
    break
  else:
    test = 0
if test == 0:
  print("NG")
