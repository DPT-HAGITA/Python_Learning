# -----------------------------
# 1.リストの基本
# -----------------------------

#リストは　変数名 = []
#辞書は　　変数名 = {}

#リストは 複数の値をまとめて格納できるデータ型
fruits = ["apple", "banana", "orange"]

print(fruits)        # ['apple', 'banana', 'orange']
print(type(fruits))  # <class 'list'>

#変更可能というのが特徴
#要素の追加・削除・更新が自由にできる


# -----------------------------
# 2. インデックスアクセス
# -----------------------------

#インデックスは 0から始まる番号 で要素を指定する
print(fruits[0])   # apple
print(fruits[1])   # banana
print(fruits[-1])  # orange（最後の要素）
print(fruits[-2])  # banana（後ろから2番目）


# -----------------------------
# 3. 要素の追加・削除
# -----------------------------

#要素の追加・削除が動的に変更できる
fruits.append("grape")       # 末尾に追加
print(fruits)  # ['apple', 'banana', 'orange', 'grape']

fruits.insert(1, "melon")    # 指定位置に挿入（index=1）
print(fruits)  # ['apple', 'melon', 'banana', 'orange', 'grape']

fruits.remove("banana")      # 値で削除（最初に見つかったものだけ）
print(fruits)  # ['apple', 'melon', 'orange', 'grape']

del fruits[0]                # インデックス指定で削除
print(fruits)  # ['melon', 'orange', 'grape']

popped = fruits.pop()        # 末尾を取り出し＆削除
print(popped)   # grape
print(fruits)   # ['melon', 'orange']

popped = fruits.pop(0)   # インデックス0 → 先頭を取り出し＆削除
print(popped)   # melon
print(fruits)   # ['orange']


# -----------------------------
# 4. スライス（部分取り出し）
# -----------------------------

#スライスは「開始:終了[:ステップ]」で範囲を指定
numbers = [0, 1, 2, 3, 4, 5]

print(numbers[1:4])   # [1, 2, 3]（1〜3番目）
print(numbers[:3])    # [0, 1, 2]（先頭〜2番目まで）
print(numbers[2:])    # [2, 3, 4, 5]（2番目以降）
print(numbers[::2])   # [0, 2, 4]（2つ飛ばし）
print(numbers[::-1])  # [5, 4, 3, 2, 1, 0]（逆順）


# -----------------------------
# 5. 組み込み関数との相性
# -----------------------------

#リストはPython標準関数でよく使う
numbers = [1, 2, 3, 4, 5]

print(sum(numbers))                 # 15
print(max(numbers))                 # 5
print(min(numbers))                 # 1
print(sorted(numbers))              # [1, 2, 3, 4, 5]
print(sorted(numbers, reverse=True)) # [5, 4, 3, 2, 1]（逆順）


# -----------------------------
# 6. リストの便利メソッド
# -----------------------------
colors = ["red", "blue", "green", "blue"]

print(colors.count("blue"))  # 2（要素の出現回数）
print(colors.index("green")) # 2（最初に見つかった位置）

colors.sort()                # 破壊的ソート
print(colors)  # ['blue', 'blue', 'green', 'red']

colors.reverse()             # 逆順に並べ替え
print(colors)  # ['red', 'green', 'blue', 'blue']


# --------------------------------
# 7. ネストしたリスト（多次元リスト）
# --------------------------------

#リストの中にリストを入れると 表形式データを表現できる
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0])      # [1, 2, 3]（1行目）
print(matrix[1][2])   # 6（2行目3列目）


# -----------------------------
# 8. リスト内包表記（短く書ける）
# -----------------------------

#内包表記の書き方ルール
#[式 for 変数 in イテラブル if 条件]

#イテラブルについて
#「順番に中身を取り出せるもの」のこと

#リスト [1, 2, 3]
#文字列 "abc"
#タプル (10, 20, 30)
#辞書 { "a": 1, "b": 2 }（キーを順番に取り出せる）
#集合 {1, 2, 3}
#↑↑↑すべて「イテラブル」

#通常の書き方-1
squares = []
for i in range(5):
    squares.append(i**2)
print(squares)  # [0, 1, 4, 9, 16]

#内包表記-1  [式 for 変数 in イテラブル]
squares = [i**2 for i in range(5)]
print(squares)  # [0, 1, 4, 9, 16]

#通常の書き方-2
evens = []
for i in range(10):
    if i % 2 == 0:
        evens.append(i)
print(evens)  # [0, 2, 4, 6, 8]

#内包表記-2  [式 for 変数 in イテラブル if 条件]
evens = [i for i in range(10) if i % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8]


# --------------------------------------
# 9.実務でのパターン:センサーのデータ管理
# --------------------------------------

#ハウス内の温度・湿度・光量などを複数ポイントで測定する場合
# 5つのセンサーの温度データ（単位: ℃）
temperatures = [24.5, 25.0, 23.8, 24.2, 25.1]

# 平均温度
avg_temp = sum(temperatures) / len(temperatures)
print("平均温度:", avg_temp)  #平均温度: 24.52

# 25度以上のセンサーだけ抽出
high_temp_sensors = [t for t in temperatures if t >= 25]
print("高温センサー:", high_temp_sensors)  #高温センサー: [25.0, 25.1]


# --------------------------------------------
# 10.実務でのパターン:日ごとのデータ履歴をまとめる
# --------------------------------------------

#ハウス栽培では日々のデータを記録して分析する
# 1週間の湿度データ（%）
weekly_humidity = [
    [60, 62, 61],  # 月曜日 3センサー
    [59, 61, 60],  # 火曜日
    [58, 60, 59],  # 水曜日
]

# 水曜日のデータを取得
wednesday = weekly_humidity[2]
print("水曜日の湿度:", wednesday)  #水曜日の湿度: [58, 60, 59]

# 全センサーの平均湿度
avg_humidity = [sum(day)/len(day) for day in weekly_humidity]
print("1週間の平均湿度:", avg_humidity)  #1週間の平均湿度: [61.0, 60.0, 59.0]


# ----------------------------------
# 11.実務でのパターン:植物の状態管理
# ----------------------------------

#各植物の成長ステータスをリストで管理する例
#リストと辞書の組み合わせ↓
plants = [
    {"name": "トマト", "height": 15, "watered": True},
    {"name": "ナス", "height": 12, "watered": False},
    {"name": "キュウリ", "height": 18, "watered": True}
]

# 水やりしていない植物だけ抽出
dry_plants = [p["name"] for p in plants if not p["watered"]]
print("水やり必要:", dry_plants)  #水やり必要: ['ナス']

# 成長が15cm以上の植物
tall_plants = [p["name"] for p in plants if p["height"] >= 15]
print("背の高い植物:", tall_plants)  #背の高い植物: ['トマト', 'キュウリ']


# ---------------------------------------
# 12.実務でのパターン:アラート・通知用リスト
# ---------------------------------------

#条件に合う植物やセンサーをまとめて通知する場合
temperatures = [24.5, 25.0, 23.8, 24.2, 25.1]  # 5つのセンサーの温度データ（単位: ℃）
alerts = []

# 温度が高いセンサー
for i, t in enumerate(temperatures):
    if t >= 25:
        alerts.append(f"センサー{i+1} 高温注意: {t}℃")

print(alerts)  #['センサー2 高温注意: 25.0℃', 'センサー5 高温注意: 25.1℃']
