"""
Problem Statement
We have 
N cards. A number 
a 
i
​
  is written on the 
i-th card.
Alice and Bob will play a game using these cards. In this game, Alice and Bob alternately take one card. Alice goes first.
The game ends when all the cards are taken by the two players, and the score of each player is the sum of the numbers written on the cards he/she has taken. When both players take the optimal strategy to maximize their scores, find Alice's score minus Bob's score.

Constraints
N is an integer between 
1 and 
100 (inclusive).
a 
i
​
  (1≤i≤N) is an integer between 
1 and 
100 (inclusive).
"""

n = int(input())
a = list(map(int, input().split()))
a = sorted(a, reverse=True)
 
alice =[]
bob = []
 
for i in range(1,n+1):
  if i % 2 != 0:
    alice.append(a[i-1])
  elif i % 2 == 0:
    bob.append(a[i-1])
    
print(sum(alice) - sum(bob))


--------------------------------

n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)

result = 0

for i in range(n):
  if i %2 == 0:
    result += a[i]
  else:
    result -= a[i]

print(result)
