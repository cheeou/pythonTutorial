s = 'First line.\nSecond line.'
print(s)

print(r'C:\some\name') # 最初の引用符の前にraw string付けるとそのまま文字出力される
# print('C:\some\name')

text = ('長い文字列を改行したい時は'
        'この方法役に立つ。')
print(text)

# 変数どうし、変数とリテラル連結したい場合’＋’を使う。
print(text + 'great')

""" 文字列は「インデックス」を指定して文字を取得できる。最初の文字のインデックスは０になる。
    専用のデータ型はなして単に長さが「１」の文字である。
"""
word = 'Python'
print(word[0])

# 負の値は右から数える
print(word[-1]) #　-０は０と区別できないから負のインデックスは-１から始まる。
print(word[::-1])

# 最初のインデックスを省略すると０と見なされる
print(word[:2])
# 二番目のインデックス(終了するインデックス)を省略すると最後の文字列までスライスする。
print(word[4:])
print(word[-2:])

# 開始値は常に含まれ、終了値は常に含まれないことにご注意。s[:i] + s[i:]は常にsとひとしくなる
print(word[:2] + word[2:])

# 文字列のインデックスに代入するとエラーが発生する
# 元の文字列と別の文字列が必要な場合、新しく文字列を作成する
print('J' + word[1:])

# 組み込み関数len()は文字列の長さを返す。
print(len(word))

# 文字列内の要素の数を数えるために使用。aの文字列の中で'b'の出現回数を数えてリターン
a = "hobby"
print(a.count('b'))

# 文字列の検索
print('bb' in a)
print('zz' not in a)

# 文字列の位置の検索
# find 最初にマッチングしたインデックスを返す。マッチングしない場合は-1を返す。
print(a.find('b')) # start 0

# index関数はfindと異なるポイントはマッチングしたい文字を検索する場合、エラーが発生する。
# print(a.index('j'))

#'間に挿入する文字列'.join[連結するリストもしくは文字列]
print(f"a>>{a}")
print(' '.join(a)) # h o b b y

print(a.upper())
print(a.lower())

# lstrip(remove left space), rstrip(remove right space), strip(remove both sides strip)

# 文字列を変える
new_s = a.replace("hobby", "happy")
print(f"new one>>>{new_s}")

# split()で分割するとlistを再び一つの文字列に連結するにはjoin()を使う。
s_blank = 'one two   three\nfour\tfive'
new_sb = s_blank.split()
print(new_sb) # type of list
print(type(','.join(new_sb))) # type of str

# 注意！文字列の組み込みの関数は変数の値を変えることはできない。再び代入しなければならない。
