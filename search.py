import pandas as pd
import eel

### 鬼滅サーチのデスクトップアプリ
def kimetsu_search(word, csv_name):
  # 検索対象取得
  df = pd.read_csv("./{}".format(csv_name))
  source = list(df["name"])

  #検索
  if word in source:
    print("「{}」はいます".format(word))
    eel.view_log_js("「{}」はいます".format(word))
  else:
    print("「{}」はいません".format(word))
    eel.view_log_js("「{}」はいません".format(word))
    eel.view_log_js("「{}」を追加します".format(word))
    source.append(word)

  # csv書き込み
  df = pd.DataFrame(source, columns=["name"])
  df.to_csv("./{}".format(csv_name), encoding= "utf-8-sig")