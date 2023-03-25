"""
Problem Statement
There are 
N positive integers written on a blackboard: 
A 
1
​
 ,...,A 
N
​
 .

Snuke can perform the following operation when all integers on the blackboard are even:

Replace each integer 
X on the blackboard by 
X divided by 
2.
Find the maximum possible number of operations that Snuke can perform.

Constraints
1≤N≤200
1≤A 
i
​
 ≤10 
9
"""

n = int(input())
a = list(map(int, input().split()))
counter = 0

keep_going = True

while True:
  for num in a:
    if num % 2 == 1:
      keep_going = False
  if not keep_going:
      break
  for i in range(n):
      a[i-1] //= 2
  counter += 1

print(counter)

------------------------------
n = int(input())
a = list(map(int, input().split()))
counter = 0

keep_going = True

while all(num%2==0 for num in a):
  a = [num//2 for num in a]
  counter += 1
print(counter)
