"""
問題文
1 以上 
N 以下の整数のうち、
10 進法での各桁の和が 
A 以上 
B 以下であるものの総和を求めてください。

制約
1≤N≤10 
4
 
1≤A≤B≤36
入力はすべて整数である
"""


nab = input().split()
n = nab[0]
a = int(nab[1])
b = int(nab[2])
total = 0

for i in range(int(n)+1):
    n_num = [int(num) for num in str(i)]
    n_num = sum(n_num)
    if n_num >= a and n_num <= b:
        total += i
    else:
        continue

print(total)
