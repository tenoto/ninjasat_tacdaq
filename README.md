# ninjasat_tacdaq
Data Acquisition Board for the NinjsSat 


正常に読み出せていれば、

1613382339.914022,P,512,695,1045,
1613382339.915853,S,38,40,41,42,43,43,43,43,44,44,44,44,44,44,44,43,43,42,42,42,42,41,41,40,40,39,39,38,38,38,38,38,38,37,37,37,37,37,36,36,36,35,35,

のようになります。

1 列目は、読み出した Mac でつけている時刻情報 unixtime です。

2 列目はフラグが来て、フラグの後ろはそれぞれ以下です。(ただし、現在書き込まれているファームウェアの場合)
M = HK データ (ADC-ch1, ADC-ch2, "A", 低速ADC-ch1〜8)
P = イベントデータ (波高値, 積算値A, 積算値B)
S = オシロスコープデータ (20 ns ごとの波高値)

いただいた最新のファームウェアにすると (今日物品の準備が終わったらする予定)、タイムカウンタ (ロング, ショート) のコラムが追加されます。
タイムカウンタの入る位置はフラグごとに少し異なり、M フラグには先頭に 2 列、P フラグでは最後に 2 列入ることになります。
S フラグには入りません。

また M フラグの出力が変わって、後ろにさらに内部温度, 内部電圧のコラムが追加されています。

さらに L フラグが追加されています。
GPS を取得したときのタイムカウンタ 2 列 (ショートはリセット前の値) が出てくるはずです。

なお、どれかファイルを開いて先頭行付近を見ていただくとわかりますが、
たいてい読み出し開始直後は出力がバグります。これは原因不明です。
とりあえずは所定のフォーマットになるところまで、スキップして解析に回す方針で考えています。


https://riken-share.box.com/s/ba1hbjom2nivg009j4fskgr7nu443yom
read_effuluent という関数の中がフラグ処理とファイルダンプです。
