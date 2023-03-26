"""
Problem Statement
You are given an 
H×W grid.
The squares in the grid are described by 
H strings, 
S 
1
​
 ,...,S 
H
​
 .
The 
j-th character in the string 
S 
i
​
  corresponds to the square at the 
i-th row from the top and 
j-th column from the left 
(1≤i≤H,1≤j≤W).
. stands for an empty square, and # stands for a square containing a bomb.

Dolphin is interested in how many bomb squares are horizontally, vertically or diagonally adjacent to each empty square.
(Below, we will simply say "adjacent" for this meaning. For each square, there are at most eight adjacent squares.)
He decides to replace each . in our 
H strings with a digit that represents the number of bomb squares adjacent to the corresponding empty square.

Print the strings after the process.

Constraints
1≤H,W≤50
S 
i
​
  is a string of length 
W consisting of # and ..
"""

DX = [1, 0, -1, 0, 1, -1, -1, 1]
DY = [0, 1, 0, -1, 1, 1, -1, -1]

h,w = map(int, input().split())
s = [input() for i in range(h)]

result = [[0 if v=='.' else "#" for v in row]for row in s]

for i in range(h):
  for j in range(w):
    if s[i][j] != '.':
      continue

    for dx, dy in zip(DX, DY):
      ni, nj = i +dx, j +dy

      if ni < 0 or ni >=h or nj<0 or nj >= w:
        continue
      if s[ni][nj] == "#":
        result[i][j] += 1

for row in result:
  print(*row, sep='')
