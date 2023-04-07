import json

define = {
    #耐久値
    "number" : 251 ,
    #モデルのファイル名(minecraft基準)
    "prefix" : "standard/ip",
    #アイテム名(id)
    "itemname" : "iron_pickaxe",
    #数字の丸め方。
    "numsize" : 3, 
    #少数の丸め方
    "flosize" : 16
}
#呼び出し
call_set = "standard_2"
#デバッグモード
debug = False

#呼び出し用
if call_set == "none":
    pass
elif call_set == "standard":
    define["number"] = 33
    define["itemname"] = "golden_pickaxe"
    define["prefix"] = "standard/gp"
    define["numsize"] = 2
elif call_set == "standard_2":
    define["number"] = 33
    define["itemname"] = "golden_axe"
    define["prefix"] = "standard/ga"
    define["numsize"] = 2
elif call_set == "dailys":
    define["number"] = 251
    define["itemname"] = "iron_pickaxe"
    define["prefix"] = "dailys/ip"
    define["numsize"] = 3

#変更があった場合は変更
itemid = "item/" + define["itemname"]
#ダメージ値の丸め方
damage_num = "{0:." + str(define["flosize"]) + "f}"
#モデル番号の丸め方
item_num = "{:0>" + str(define["numsize"]) + "}" 

#主なもの
#for i in range(number):
#    x=round(1/number*i,6)
#    y="{0:.6f}".format(x)
#    z="{:0>3}".format(i)
#    print(z+":"+y)
#楽だね

#デバッグ用表示
if(debug==True):
    print("[debug] 設定内容")
    print(define)
    print("耐久値:"+str(define["number"]))
    print("アイテム名:"+str(itemid))
    print("モデル名:"+str(define["prefix"])+item_num.format(1))
    print("耐久値出力:"+damage_num.format(round(1/define["number"]*1,define["flosize"])))

#配列作成
overrides = []
#指定したnumber値まで大量生成
#range 指定した番号まで配列を生成してくれる。 
for i in range(define["number"]+1):
    #耐久値が最大の時は標準にする。
    if(i==0):
        override = {
            "predicate": {
                "damaged": 0,
                "damage": 0
            },
            "model": itemid
        }
    else:
        #適当に数字丸める。
        #耐久値割合 = 1 / 最大耐久値 * 耐久値
        x=float(damage_num.format(round(1/define["number"]*i,define["flosize"])))
        #モデル名
        z=define["prefix"] + item_num.format(i) 
        #ダメージ値とモデル名を入れる。
        override = {
            "predicate": {
               "damaged": 0,
                "damage": x
           },
            "model": z
        }
    #append 配列の末端に追加する。
    #上で作った辞書型データを入れる。
    overrides.append(override)

#最後に破壊後のデータを入れる。
overrides.append({"predicate": {"damaged": 1, "damage": 0}, "model": itemid })

#残りの分を入れる。
json_file={
    "parent":"item/handheld",
    "textures": {
        "layer0": itemid
    },
    "overrides": overrides
}

#debug用
if(debug==True):
    print("[debug] 辞書型データ表示")
    print(json_file)

#jsonに直す
json_dump=json.dumps(json_file)

#debug用
if(debug==True):
    print("[debug] jsonのダンプ表示")
    print(json_dump)

#出力
#mode="w" 上書きもしくは新規作成
#with 仮変数を作って、入れてくれる。 他のところでは使えない。
#str 文字列型に直してくれる
path = "./"+ define["itemname"] + ".json"
with open(path,mode="w") as f:
    f.write(str(json_dump))