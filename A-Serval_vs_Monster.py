"""
問題文
サーバルはモンスターと戦っています。

モンスターの体力は 
H です。

サーバルが攻撃を 
1 回行うとモンスターの体力を 
A 減らすことができます。 攻撃以外の方法でモンスターの体力を減らすことはできません。

モンスターの体力を 
0 以下にすればサーバルの勝ちです。

サーバルがモンスターに勝つために必要な攻撃の回数を求めてください。

制約
1≤H≤10 
4
 
1≤A≤10 
4
 
入力中のすべての値は整数である。
"""

h, a = map(int, input().split())
time = 0
while h > 0:
  h -= a
  time += 1
print(time)

--------------------------------

h, a = map(int, input().split())
if h % a == 0:
  print(h//a)
else:
  print(h//a + 1)
