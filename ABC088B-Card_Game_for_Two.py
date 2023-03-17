"""
問題文
N 枚のカードがあります. 
i 枚目のカードには, 
a 
i
​
  という数が書かれています.
Alice と Bob は, これらのカードを使ってゲームを行います. ゲームでは, Alice と Bob が交互に 1 枚ずつカードを取っていきます. Alice が先にカードを取ります.
2 人がすべてのカードを取ったときゲームは終了し, 取ったカードの数の合計がその人の得点になります. 2 人とも自分の得点を最大化するように最適な戦略を取った時, Alice は Bob より何点多く取るか求めてください.

制約
N は 
1 以上 
100 以下の整数
a 
i
​
  (1≤i≤N) は 
1 以上 
100 以下の整数
"""

alice = []
bob = []

num = input()
cards = input().split()
cards = sorted([int(num) for num in cards], reverse=True)
times = 1

for card in cards:
    if times % 2 != 0:
        alice.append(int(card))
    else:
        bob.append(int(card))
    times += 1

print(sum(alice)-sum(bob))
