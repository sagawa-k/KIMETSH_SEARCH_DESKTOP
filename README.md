# KIMETSH_SEARCH_DESKTOP  

view.pyがメインの実行ファイル。これを実行するとデスクトップアプリが表示。

# 1
HTML使い検索ワード入力と検索ボタンを作成
htmlフォルダ内のindex.htmlに対してHTMLタグを用いて追加

# 2
検索ワード入力が空だったらアラートを表示させ、検索はしない

# 3
検索結果をデスクトップアプリの画面に表示できるようにtextareaタグを使って
ログ表示領域を作成

# 4
作成したログ表示領域にkimetsu_searchの結果を表示

# 5
ログ表示領域が小さいので大きく表示できるようにclassを定義して、style.cssに処理を記述

# 6
CSVファイルの保存先をHTML画面から指定

# 7
Pyinstallerを使って、１つの実行可能ファイルにパッケージ化。  
pipでインストール後に以下コマンドを実行。
distフォルダに実行可能フィイルが格納される。
顧客提供時は、このファイルを提供することでpythonのインストールは不要。
`python -m eel <はじめに起動するpyファイル> <htmlのフォルダ名> --onefile`