
# Table of Contents

-   [はじめに](#org5cf6f59)
-   [1. 準備](#orgb46ee93)
    -   [1.1. パーツ・工具の確認](#org983a6b0)
        -   [1.1.1 キットに含まれるパーツ・工具](#org31cf02f)
        -   [1.1.2. ご自身でご用意いただくパーツ・工具](#org3f97b51)
    -   [1.2. PCBの動作確認](#orgbc9a5dc)
        -   [1.2.1. Vial環境の準備](#orgf739123)
        -   [1.2.2. ファームウェア書き込み](#orgaefd5c4)
        -   [1.2.3. Vialを起動](#org67e280b)
-   [2. 組み立て](#orgc077d62)
    -   [2.1. レイアウトの選択](#org644d39d)
        -   [2.1.1. スタビライザーの取り付け](#org8ccff0b)
        -   [2.1.2. ロータリーエンコーダーの取り付け](#org251913c)
    -   [2.2. スイッチプレート取り付け](#orgcba5a83)
    -   [2.3. PCB取り付け](#org80abc09)
    -   [2.4. ドーターボード取り付け](#org388ae51)
    -   [2.5. 動作確認](#orgcb474f4)
    -   [2.6. キーキャップ取り付け](#orgfd49e0b)
-   [3. キーマップの設定](#org4d59cc9)
-   [4. メンテナンス](#org62f6afb)
    -   [4.1. ファームウェア更新](#org904e120)
-   [5. トラブルシューティング](#org548d13e)
    -   [5.1. 反応しないキーがある](#orgc7e5c92)
        -   [5.1.1. キーボードを認識しない](#org64106ef)
        -   [5.1.2. キースイッチが反応しない](#orgae28df2)
        -   [5.1.3. ロータリーエンコーダーが反応しない](#org2307b14)
-   [6. 連絡先](#org23884ea)
-   [さいごに](#orgab90407)



<a id="org5cf6f59"></a>

# はじめに

Yak40をお買い上げいただきありがとうございます。  
決して難しい構造ではありませんが、このドキュメントを良く読んで組み立ててください。  
Yak40によって、あなたのキーボードライフが少しでも楽しいものになればこれに勝る喜びはありません。


<a id="orgb46ee93"></a>

# 1. 準備


<a id="org983a6b0"></a>

## 1.1. パーツ・工具の確認


<a id="org31cf02f"></a>

### 1.1.1 キットに含まれるパーツ・工具

キットには以下のパーツ・工具が含まれています。  
不足がある場合は[6. 連絡先](#org23884ea)までご連絡ください。

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-right" />

<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">名称</th>
<th scope="col" class="org-right">数量</th>
<th scope="col" class="org-left">画像</th>
<th scope="col" class="org-left">説明</th>
</tr>
</thead>

<tbody>
<tr>
<td class="org-left">ケース</td>
<td class="org-right">1</td>
<td class="org-left"><img src="./images/top_case.png" alt="top_case.png" /></td>
<td class="org-left">CNC切削アルミケース。</td>
</tr>


<tr>
<td class="org-left">ボトムプレート</td>
<td class="org-right">1</td>
<td class="org-left"><img src="./images/bottom_plate.png" alt="bottom_plate.png" /></td>
<td class="org-left">ケースの底板。</td>
</tr>


<tr>
<td class="org-left">PCB</td>
<td class="org-right">1</td>
<td class="org-left"><img src="./images/pcb.png" alt="pcb.png" /></td>
<td class="org-left">キーボードの本体となる基板。パーツはすべて実装済みです。</td>
</tr>


<tr>
<td class="org-left">ドーターボード</td>
<td class="org-right">1</td>
<td class="org-left"><img src="./images/udb_s1.png" alt="udb_s1.png" /></td>
<td class="org-left">USBコネクター部分の基板。</td>
</tr>


<tr>
<td class="org-left">ドーターボードケーブル</td>
<td class="org-right">1</td>
<td class="org-left"><img src="./images/udb_cable.png" alt="udb_cable.png" /></td>
<td class="org-left">PCBとドータボードを接続するためのケーブル。</td>
</tr>


<tr>
<td class="org-left">スイッチプレート</td>
<td class="org-right">1</td>
<td class="org-left"><img src="./images/switch_plate.png" alt="switch_plate.png" /></td>
<td class="org-left">キースイッチを固定するためのプレート。</td>
</tr>


<tr>
<td class="org-left">ミドルフォーム</td>
<td class="org-right">1</td>
<td class="org-left"><img src="./images/middle_foam.png" alt="middle_foam.png" /></td>
<td class="org-left">スイッチプレートとPCBの間に挟む4mm厚のPORONフォーム。袋から取り出しづらいため、慎重に取り出してください。</td>
</tr>


<tr>
<td class="org-left">バーガーマウント用Oリング</td>
<td class="org-right">20(予備4)</td>
<td class="org-left"><img src="./images/o_ring.png" alt="o_ring.png" /></td>
<td class="org-left">バーガーマウント用のシリコンOリング。</td>
</tr>


<tr>
<td class="org-left">M2x3.5 スペーサー</td>
<td class="org-right">9(予備2)</td>
<td class="org-left"><img src="./images/standoff.png" alt="standoff.png" /></td>
<td class="org-left">スイッチプレートとPCBを固定するための4mm径のスペーサ。</td>
</tr>


<tr>
<td class="org-left">M2x3 低頭ねじ</td>
<td class="org-right">16(予備2)</td>
<td class="org-left"><img src="./images/low_head_m2l3.png" alt="low_head_m2l3.png" /></td>
<td class="org-left">スイッチプレートにPCBを取り付けるためのねじ。</td>
</tr>


<tr>
<td class="org-left">M2x5 トラスねじ</td>
<td class="org-right">10(予備2)</td>
<td class="org-left"><img src="./images/truss_m2l5.png" alt="truss_m2l5.png" /></td>
<td class="org-left">ケースにスイッチプレートを取り付けるためのねじ。</td>
</tr>


<tr>
<td class="org-left">M3x6 低頭ねじ</td>
<td class="org-right">2(予備1)</td>
<td class="org-left"><img src="./images/low_head_m3l6.png" alt="low_head_m3l6.png" /></td>
<td class="org-left">ドーターボードをケースに取り付けるためのねじ。</td>
</tr>


<tr>
<td class="org-left">M3x4 なべねじ</td>
<td class="org-right">8(予備1)</td>
<td class="org-left"><img src="./images/pan_m3l4.png" alt="pan_m3l4.png" /></td>
<td class="org-left">ケースにボトムプレートを取り付けるためのねじ。</td>
</tr>


<tr>
<td class="org-left">ゴム足</td>
<td class="org-right">8(予備4)</td>
<td class="org-left"><img src="./images/rubber_feet.png" alt="rubber_feet.png" /></td>
<td class="org-left">ボトムプレートに貼り付ける滑り止め。</td>
</tr>


<tr>
<td class="org-left">+ドライバー</td>
<td class="org-right">1</td>
<td class="org-left"><img src="./images/screwdriver.png" alt="screwdriver.png" /></td>
<td class="org-left">ねじを締め付けるために使用します。</td>
</tr>
</tbody>
</table>


<a id="org3f97b51"></a>

### 1.1.2. ご自身でご用意いただくパーツ・工具

キット以外に以下のパーツが必要になります。  
ご自身でお気に入りのものをご用意ください。

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">名称</th>
<th scope="col" class="org-left">数量</th>
<th scope="col" class="org-left">説明</th>
</tr>
</thead>

<tbody>
<tr>
<td class="org-left">MX(互換)キースイッチ</td>
<td class="org-left">41から46</td>
<td class="org-left">選択したレイアウトに応じて必要な個数をご用意ください。</td>
</tr>


<tr>
<td class="org-left">PCBマウント MX(互換)スタビライザー 2U</td>
<td class="org-left">0から3</td>
<td class="org-left">選択したレイアウトに応じてお好みでご用意ください。</td>
</tr>


<tr>
<td class="org-left">EC12(互換)ロータリーエンコーダー</td>
<td class="org-left">0から2</td>
<td class="org-left">選択したレイアウトに応じて必要な個数をご用意ください。ロータリーエンコーダーを取り付ける場合ははんだ付けが必要になります。</td>
</tr>


<tr>
<td class="org-left">MX(互換)キーキャップ</td>
<td class="org-left">1セット</td>
<td class="org-left">お好きなものをご用意ください。ただし、選択したレイアウトに応じてキースイッチの南向き、北向きが混在するため、キーキャップによってキースイッチと干渉する可能性があります。</td>
</tr>


<tr>
<td class="org-left">USB Type-Cケーブル</td>
<td class="org-left">1</td>
<td class="org-left">お好きなものをご用意ください。ただし、コネクター部分の形状によっては奥まで挿し込めない可能性があります。</td>
</tr>


<tr>
<td class="org-left">はんだごて</td>
<td class="org-left">一式</td>
<td class="org-left">ロータリーエンコーダーを取り付けたい場合はご用意ください。一般的な電子工作用のはんだごてで十分です。</td>
</tr>


<tr>
<td class="org-left">はんだ</td>
<td class="org-left">適量</td>
<td class="org-left">ロータリーエンコーダーを取り付けたい場合はご用意ください。</td>
</tr>
</tbody>
</table>


<a id="orgbc9a5dc"></a>

## 1.2. PCBの動作確認


<a id="orgf739123"></a>

### 1.2.1. Vial環境の準備

キーマップの変更にはVial( <https://get.vial.today> )を使用します。  
以下のいずれかの環境をご用意ください。

-   Web版（最新のChrome、Chromium、Edge推奨）
-   デスクトップアプリ版


<a id="orgaefd5c4"></a>

### 1.2.2. ファームウェア書き込み

1.  以下のURLからYak40のファームウェアをダウンロードする
    -   <https://github.com/kuriki-sasa/vial-qmk/releases>
        ![img](./images/download_firmware.png)
2.  PCBとドーターボードをドーターボードケーブルで接続する
3.  USB Type-CケーブルでPCとドーターボードを接続する
    -   PCにUSBストレージとして認識されます。
4.  認識したUSBストレージにダウンロードしたファームウェアをコピーする
    -   コピーが完了すると自動でUSBストレージが取り出され、キーボードとして認識されます。


<a id="org67e280b"></a>

### 1.2.3. Vialを起動

Web版、またはデスクトップアプリ版Vialを起動し、キーボードが認識されていることを確認してください。  
認識しない場合はは[5. トラブルシューティング](#org548d13e)をご確認ください。  
確認が完了したらPCから取り外し、PCB、ドーターボード、ドーターボードケーブルに分解します。


<a id="orgc077d62"></a>

# 2. 組み立て


<a id="org644d39d"></a>

## 2.1. レイアウトの選択

組み立て後にスタビライザー、またはロータリーエンコーダーを取り付けることはできないため、この時点で[対応レイアウト](https://www.keyboard-layout-editor.com/#/gists/28697eab129d40e1805bf8ff4fb0f721)から使いたいレイアウトを選択します。  
スタビライザー、またはロータリーエンコーダーを取り付けない場合は組み立て後からもレイアウトを変更できるため、この項目はスキップしてください。


<a id="org8ccff0b"></a>

### 2.1.1. スタビライザーの取り付け

使いたいレイアウトに応じて以下の位置にスタビライザーを取り付けます。
![img](./images/install_stabilizers.jpg)


<a id="org251913c"></a>

### 2.1.2. ロータリーエンコーダーの取り付け

使いたいレイアウトに応じて以下の位置にロータリーエンコーダーをはんだ付けします。
![img](./images/install_rotary_encoders.jpg)


<a id="orgcba5a83"></a>

## 2.2. スイッチプレート取り付け

1.  スイッチプレートの表裏に注意し、 `M2x3 低頭ねじ` でスペーサーを取り付ける
    ![img](./images/install_standoffs.jpg)
2.  ケースの赤丸の位置にOリングを乗せる
    ![img](./images/puton_o_rings.jpg)
3.  ケースにスイッチプレートを乗せる
    -   Oリングがずれやすいため慎重に乗せてください。
4.  `M2x5 トラスねじ` にOリングを通し、ケースにスイッチプレートを取り付ける
    ![img](./images/install_switch_plate.jpg)
    ![img](./images/install_switch_plate_drawing.png)
    -   ゆるすぎると使用中にスイッチプレートが外れ、逆に強く締めすぎると打鍵感が固くなります。  
        適度な力で締め付けてください。


<a id="org80abc09"></a>

## 2.3. PCB取り付け

1.  スイッチプレートにフォームを置く
    ![img](./images/install_mid_foam.jpg)
    -   袋から取り出しづらいため、無理に引っ張らず、慎重に取り出してください。
2.  スイッチプレートに `M2x3 低頭ねじ` でPCBを取り付ける
    ![img](./images/install_pcb.jpg)
    -   スペーサーの高さよりもフォームのほうが少し厚くなっています。  
        指でPCBをスイッチプレート側に押しながらねじを締めてください。


<a id="org388ae51"></a>

## 2.4. ドーターボード取り付け

1.  ケースに `M3x6 低頭ねじ` でドーターボードを取り付ける
    ![img](./images/install_daughterboard.jpg)
2.  PCBとドーターボードをドーターボードケーブルで接続する


<a id="orgcb474f4"></a>

## 2.5. 動作確認

1.  ケースを裏返し、キースイッチを取り付ける
    ![img](./images/install_switches.jpg)
2.  USB Type-CケーブルでPCとYak40キーボードを接続する
3.  Web版、またはデスクトップアプリ版Vialを起動する
4.  `Layout` タブを表示し、レイアウトを選択する
    ![img](./images/layout_settings.png)
    -   ドロップダウンメニューからご自身のYak40のレイアウトを選択してください。
5.  `Matrix tester` タブを表示し、 `Unlock` ボタンをクリックする
    ![img](./images/unlock1.png)
6.  表示された二箇所のキーを長押しする
    ![img](./images/unlock2.png)
    -   キーを押しているのに進捗バーが進まない場合、キーが反応していない可能性があります。  
        [5. トラブルシューティング](#org548d13e)をご確認ください。
7.  全キーが反応することを確認する
    ![img](./images/test_matrix.png)
    -   反応しないキーがある場合は[5. トラブルシューティング](#org548d13e)をご確認ください。


<a id="orgfd49e0b"></a>

## 2.6. キーキャップ取り付け

用意したお気に入りのキーキャップを取り付けてください。  
もう少しで完成です。


<a id="org4d59cc9"></a>

# 3. キーマップの設定

`Keymap` タブを表示し、お好みのキーマップを設定してください。  
画面上部から変更したいキーをクリックし、その後、設定したいキーを画面下部から選択します。
![img](./images/change_keymap.png)


<a id="org62f6afb"></a>

# 4. メンテナンス


<a id="org904e120"></a>

## 4.1. ファームウェア更新

1.  ボトムプレートを取り外す
2.  USB Type-CケーブルでPCとYak40キーボードを接続する
3.  PCBの `BOOT` スイッチを押しながら `RESET` スイッチを押す
    -   PCにUSBストレージとして認識されます。
4.  認識したUSBストレージに新しいファームウェアをコピーする
    -   コピーが完了すると自動でUSBストレージが取り出され、キーボードとして認識されます。
5.  ボトムプレートを取り付ける


<a id="org548d13e"></a>

# 5. トラブルシューティング


<a id="orgc7e5c92"></a>

## 5.1. 反応しないキーがある


<a id="org64106ef"></a>

### 5.1.1. キーボードを認識しない

以下手順を順番に試してください。

1.  ドーターボードとPCBの接続を確認する
    -   ドーターボード・PCB両方のソケットの奥までコネクターが挿さっていることを確認してください。
2.  USB Type-Cケーブルが奥まで挿さっているか確認する
    -   コネクター部分の形状によってはケースと干渉する可能性があります。  
        他のUSB Type-Cケーブルでの接続もお試しください。
3.  [6. 連絡先](#org23884ea)に連絡する
    -   お手数をおかけしますが、連絡先のいずれかから私に連絡をしてください。  
        その際詳しい症状・写真も添付していただけますとありがたいです。


<a id="orgae28df2"></a>

### 5.1.2. キースイッチが反応しない

以下手順を順番に試してください。

1.  反応しないキーのスイッチを外す
2.  キースイッチの足が曲がっていないことを確認する
    -   足が曲がっていた場合は新しいキースイッチに交換するか、足を真っ直ぐに修正してから再度取り付けてください。
3.  キースイッチが正しく挿さっていることを確認する
    -   キースイッチがスイッチプレートから浮いている場合は、浮かないように奥まで挿してください。
4.  [6. 連絡先](#org23884ea)に連絡する
    -   お手数をおかけしますが、連絡先のいずれかから私に連絡をしてください。  
        その際詳しい症状・写真も添付していただけますとありがたいです。


<a id="org2307b14"></a>

### 5.1.3. ロータリーエンコーダーが反応しない

以下手順を順番に試してください。

1.  正しくはんだ付けできていることを確認する
    -   キーソケットとの共存のため、はんだ付け部分(パッド)が小さくなっています。  
        再度はんだごてでパッドを熱し、はんだ付けできていることを確認してください。
2.  [6. 連絡先](#org23884ea)に連絡する
    -   お手数をおかけしますが、連絡先のいずれかから私に連絡をしてください。  
        その際詳しい症状・写真も添付していただけますとありがたいです。


<a id="org23884ea"></a>

# 6. 連絡先

-   X(Twitter): [@kuriki<sub>sasa</sub>](https://x.com/kuriki_sasa)
-   Bluesky: [@kurikisasa.bsky.social](https://bsky.app/profile/kurikisasa.bsky.social)
-   Discord: kurikisasa
-   Discord server: <https://discord.gg/pC4t9NJStE>


<a id="orgab90407"></a>

# さいごに

無事、完成できましたでしょうか？  
Yak40の設計データは全て[GitHub](https://github.com/kuriki-sasa/Yak40)で公開しています。  
自分で製造するもよし、参考にしてオリジナルを作るもよし、ライセンス範囲内でお好きにご活用ください。  
良きキーボードライフを！

