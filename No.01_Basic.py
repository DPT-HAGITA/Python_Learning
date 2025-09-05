# -----------------------------
# 1. 「変数とデータ型」の基本
# -----------------------------

# 整数 (int)
a = 10
print("整数 a:", a, type(a))

# 小数 (float)
b = 3.14
print("小数 b:", b, type(b))

# 文字列 (str)
name = "Hagita"
greeting = 'Hello'
print("文字列 name:", name, type(name))
print("文字列 greeting:", greeting, type(greeting))

# 真偽値 (bool)
flag = True
print("真偽値 flag:", flag, type(flag))

# None（何もない値を表す特別な型）
empty = None
print("None型 empty:", empty, type(empty))

#リスト（list）
#複数の値を順番に入れられる「箱」(追加、変更、削除、入れ替えなど自由)
numbers = [1, 2, 3, 4]
print(numbers, type(numbers))   # [1, 2, 3, 4] <class 'list'>

#タプル（tuple）
#リストに似ているけど「変更できない」
point = (10, 20)
print(point, type(point))       # (10, 20) <class 'tuple'>

#辞書（dict）
#「キーと値」をセットで管理できる
person = {"name": "Hagita", "age": 30}
print(person, type(person))     # {'name': 'Hagita', 'age': 30} <class 'dict'>

#集合（set）
#重複を許さない「集まり」
fruits = {"apple", "banana", "apple"}
print(fruits, type(fruits))     # {'apple', 'banana'} <class 'set'>

# -----------------------------
# 2. 型変換 (Casting)
# -----------------------------

# int → float
print("int → float:", float(a))

# float → int （小数点以下切り捨て）
print("float → int:", int(b))

# 数値 → 文字列
print("int → str:", str(a))

# 文字列 → 数値（変換可能な場合のみ）
num_str = "123"
print("str → int:", int(num_str))
print("str → float:", float(num_str))

# -----------------------------
# 3. 四則演算と演算子
# -----------------------------

x, y = 7, 3
print("加算:x + y =", x + y)   # 加算
print("減算:x - y =", x - y)   # 減算
print("乗算:x * y =", x * y)   # 乗算
print("除算（float）:x / y =", x / y)   # 除算（float）
print("整数除算:x // y =", x // y) # 整数除算
print("剰余:x % y =", x % y)   # 剰余
print("累乗:x ** y =", x ** y) # 累乗

# -----------------------------
# 4. 文字列のいろいろ
# -----------------------------

text = "Python"

# インデックスアクセス（0から始まる）
print("text[0] =", text[0])   # P
print("text[-1] =", text[-1]) # n（最後の文字）

# スライス
print("text[0:3] =", text[0:3]) # Pyt
print("text[:4] =", text[:4])   # Pyth
print("text[2:] =", text[2:])   # thon
print("text[0:3] =", text[2:4]) # th

# 長さ
print("len(text) =", len(text))

# 大文字・小文字変換
print("upper:", text.upper())
print("lower:", text.lower())

# 文字列結合
print("結合:", greeting + " " + name)

# 繰り返し
print("繰り返し:", "Hi! " * 3)

# 含まれているか確認
print("'Py' in text:", "Py" in text)
print("'Java' not in text:", "Java" not in text)
print("'Hagita' in text:", "Hagita" in text)

# フォーマット
#str.format() を使う方法
print("こんにちは {} さん".format(name))
#{} がプレースホルダ（埋め込み場所）

#複数の値を入れる場合
age = 25
print("名前: {}, 年齢: {}".format(name, age))

#インデックス番号や名前で指定もできる
print("名前: {0}, 年齢: {1}".format(name, age))
print("名前: {n}, 年齢: {a}".format(n=name, a=age))

#f文字列（フォーマット文字列）
#Python 3.6 以降で使える最新で便利な方法
print(f"こんにちは {name} さん")
print(f"こんにちは {name} さん、年齢は {age} 歳です")

#文字列の中にそのまま変数や式を書ける
#計算も可能
print(f"来年は {age + 1} 歳になります")

# -----------------------------
# 5. 真偽値の基本
# -----------------------------

print("比較: 5 > 3 →", 5 > 3)
print("比較: 5 == 5 →", 5 == 5)
print("比較: 5 != 2 →", 5 != 2)

# and, or, not
#and：両方 True のときだけ True
print("True and False →", True and False)

#or :どちらかが True なら True
print("True or False  →", True or False)

#not：真偽を反転する（True → False、False → True）
print("not True       →", not True)

#Python では、数値を bool() に変換できる。（trueかfalse）
# 数値の真偽値変換（0はFalse、その他はTrue）
print("bool(0):", bool(0))
print("bool(42):", bool(42))

#if 文でよく使われる
x = 10
if x:   # xが0でなければTrue
    print("xはゼロではない！")

# 空文字列や空リストはFalse
print("bool(""):", bool(""))
print("bool([]):", bool([]))
#空のタプル ()、空の辞書 {}、空の集合 set() も False
#何か入っていれば True

#これもifでよく使う
text = ""
if not text:
    print("入力が空です")
else:
    print("入力内容:", text)


# -----------------------------
# 6. 型を確認する方法
# -----------------------------

#type(値)を使うと、そのオブジェクトがどんな型（クラス）かを返す
print("type(100):", type(100))
print("type(3.14):", type(3.14))
print("type('abc'):", type("abc"))

# isinstanceで型チェック
#isinstance(値, 型)は「その値がその型のインスタンスかどうか」を判定する
print("isinstance(100, int):", isinstance(100, int))
print("isinstance(3.14, float):", isinstance(3.14, float))
print("isinstance('abc', str):", isinstance("abc", str))
