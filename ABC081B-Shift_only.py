"""
問題文
黒板に 
N 個の正の整数 
A 
1
​
 ,...,A 
N
​
  が書かれています．

すぬけ君は，黒板に書かれている整数がすべて偶数であるとき，次の操作を行うことができます．

黒板に書かれている整数すべてを，
2 で割ったものに置き換える．
すぬけ君は最大で何回操作を行うことができるかを求めてください．

制約
1≤N≤200
1≤A 
i
​
 ≤10 
9
"""

n = int(input())
numbers = input().split()
times = 0
order = 0

list_is_even = True
while list_is_even:
    for num in numbers:
        num = int(num)
        if num % 2 == 0:
            numbers[order] = num / 2
            order += 1
        else:
            print(times)
            list_is_even = False
            break
    times += 1
    order = 0


