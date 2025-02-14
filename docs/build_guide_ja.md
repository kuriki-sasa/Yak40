
# Table of Contents

-   [はじめに](#orga48cf64)
-   [1. 準備](#orgc95d800)
    -   [1.1. パーツ・工具の確認](#org47a1902)
        -   [1.1.1 キットに含まれるパーツ・工具](#orgc534075)
        -   [1.1.2. ご自身でご用意いただくパーツ・工具](#org42209fc)
    -   [1.2. PCBの動作確認](#orgc21a704)
        -   [1.2.1. Vial環境の準備](#org002d408)
        -   [1.2.2. ファームウェア書き込み](#org23fb97c)
        -   [1.2.3. Vialを起動](#org25c0c55)
-   [2. 組み立て](#org0606cf4)
    -   [2.1. レイアウトの選択](#org24a6c72)
        -   [2.1.1. スタビライザーの取り付け](#orgcfdd90e)
        -   [2.1.2. ロータリーエンコーダーの取り付け](#orga008144)
    -   [2.2. スイッチプレート取り付け](#orgfc0ed4a)
    -   [2.3. PCB取り付け](#org8d131f3)
    -   [2.4. ドーターボード取り付け](#org1f376d5)
    -   [2.5. 動作確認](#orgbfedea7)
    -   [2.6. ボトムプレート取り付け](#org909b8ad)
    -   [2.7. キーキャップ取り付け](#org6c9f4fb)
-   [3. キーマップの設定](#orgf2ca617)
-   [4. メンテナンス](#orgd141837)
    -   [4.1. ファームウェア更新](#orgc81d1fb)
-   [5. トラブルシューティング](#org4f5d567)
    -   [5.1. キーボードがPCに認識されない](#orge0104f9)
    -   [5.2. 反応しないキーがある](#org6151273)
    -   [5.3. ロータリーエンコーダーが反応しない](#org6844cf7)
-   [6. 連絡先](#org1574eca)
-   [さいごに](#org77cd219)



<a id="orga48cf64"></a>

# はじめに

Yak40をお買い上げいただきありがとうございます。

決して難しい構造ではありませんが、このドキュメントを良く読んで組み立ててください。  
Yak40によって、あなたのキーボードライフが少しでも楽しいものになればこれに勝る喜びはありません。


<a id="orgc95d800"></a>

# 1. 準備


<a id="org47a1902"></a>

## 1.1. パーツ・工具の確認


<a id="orgc534075"></a>

### 1.1.1 キットに含まれるパーツ・工具

キットには以下のパーツ・工具が含まれています。  
不足がある場合は[6. 連絡先](#org1574eca)までご連絡ください。

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
<td class="org-left">キーボードの本体となる基板。パーツはすべて実装済みです。厚みは1.6mm。</td>
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
<td class="org-right">20(内予備4)</td>
<td class="org-left"><img src="./images/o_ring.png" alt="o_ring.png" /></td>
<td class="org-left">バーガーマウント用のシリコンOリング。</td>
</tr>


<tr>
<td class="org-left">M2x3.5 スペーサー</td>
<td class="org-right">9(内予備2)</td>
<td class="org-left"><img src="./images/standoff.png" alt="standoff.png" /></td>
<td class="org-left">スイッチプレートとPCBを固定するための4mm径のスペーサ。</td>
</tr>


<tr>
<td class="org-left">M2x3 低頭ねじ</td>
<td class="org-right">16(内予備2)</td>
<td class="org-left"><img src="./images/low_head_m2l3.png" alt="low_head_m2l3.png" /></td>
<td class="org-left">スイッチプレートにPCBを取り付けるためのねじ。</td>
</tr>


<tr>
<td class="org-left">M2x5 トラスねじ</td>
<td class="org-right">10(内予備2)</td>
<td class="org-left"><img src="./images/truss_m2l5.png" alt="truss_m2l5.png" /></td>
<td class="org-left">ケースにスイッチプレートを取り付けるためのねじ。</td>
</tr>


<tr>
<td class="org-left">M3x6 低頭ねじ</td>
<td class="org-right">3(内予備1)</td>
<td class="org-left"><img src="./images/low_head_m3l6.png" alt="low_head_m3l6.png" /></td>
<td class="org-left">ドーターボードをケースに取り付けるためのねじ。</td>
</tr>


<tr>
<td class="org-left">M3x4 なべねじ</td>
<td class="org-right">8(内予備1)</td>
<td class="org-left"><img src="./images/pan_m3l4.png" alt="pan_m3l4.png" /></td>
<td class="org-left">ケースにボトムプレートを取り付けるためのねじ。</td>
</tr>


<tr>
<td class="org-left">ゴム足</td>
<td class="org-right">8(内予備4)</td>
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


<a id="org42209fc"></a>

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
<td class="org-left">選択したレイアウトに応じてお好みでご用意ください。PCB厚1.6mm対応のものをご利用ください。</td>
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


<a id="orgc21a704"></a>

## 1.2. PCBの動作確認


<a id="org002d408"></a>

### 1.2.1. Vial環境の準備

キーマップの変更にはVial( <https://get.vial.today> )を使用します。  
以下のいずれかの環境をご用意ください。

-   Web版（最新のChrome、Chromium、Edge推奨）
-   デスクトップアプリ版


<a id="org23fb97c"></a>

### 1.2.2. ファームウェア書き込み

1.  以下のURLからYak40のファームウェアをダウンロードする
    -   <https://github.com/kuriki-sasa/vial-qmk/releases>  
        ![img](./images/download_firmware.png)
2.  PCBとドーターボードをドーターボードケーブルで接続する
3.  USB Type-CケーブルでPCとドーターボードを接続する
    -   接続後、PCにUSBストレージとして認識されます。
4.  認識したUSBストレージにダウンロードしたファームウェアをコピーする
    -   コピーが完了すると自動でUSBストレージが取り出され、キーボードとして認識されます。


<a id="org25c0c55"></a>

### 1.2.3. Vialを起動

Web版、またはデスクトップアプリ版Vialを起動し、キーボードが認識されていることを確認してください。  
認識しない場合は[5. トラブルシューティング](#org4f5d567)をご確認ください。

確認できたらPCから取り外し、PCB、ドーターボード、ドーターボードケーブルに分解します。


<a id="org0606cf4"></a>

# 2. 組み立て


<a id="org24a6c72"></a>

## 2.1. レイアウトの選択

組み立て後にスタビライザー、またはロータリーエンコーダーを取り付けることはできないため、この時点で[対応レイアウト](https://www.keyboard-layout-editor.com/#/gists/28697eab129d40e1805bf8ff4fb0f721)から使いたいレイアウトを選択します。  
スタビライザー、またはロータリーエンコーダーを取り付けない場合は組み立て後からもレイアウトを変更できるため、この項目はスキップしてください。


<a id="orgcfdd90e"></a>

### 2.1.1. スタビライザーの取り付け

使いたいレイアウトに応じて以下の位置にスタビライザーを取り付けます。  
![img](./images/install_stabilizers.jpg)


<a id="orga008144"></a>

### 2.1.2. ロータリーエンコーダーの取り付け

使いたいレイアウトに応じて以下の位置にロータリーエンコーダーをはんだ付けします。  
![img](./images/install_rotary_encoders.jpg)


<a id="orgfc0ed4a"></a>

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


<a id="org8d131f3"></a>

## 2.3. PCB取り付け

1.  スイッチプレートにフォームを置く  
    ![img](./images/install_mid_foam.jpg)
    -   袋から取り出しづらいため、無理に引っ張らず、慎重に取り出してください。
2.  スイッチプレートに `M2x3 低頭ねじ` でPCBを取り付ける  
    ![img](./images/install_pcb.jpg)
    -   スペーサーの高さよりもフォームのほうが少し厚くなっています。  
        指でPCBをスイッチプレート側に押しながらねじを締めてください。


<a id="org1f376d5"></a>

## 2.4. ドーターボード取り付け

1.  ケースに `M3x6 低頭ねじ` でドーターボードを取り付ける  
    ![img](./images/install_daughterboard.jpg)
2.  PCBとドーターボードをドーターボードケーブルで接続する


<a id="orgbfedea7"></a>

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
        [5. トラブルシューティング](#org4f5d567)をご確認ください。
7.  全キーが反応することを確認する  
    ![img](./images/test_matrix.png)
    -   反応しないキーがある場合は[5. トラブルシューティング](#org4f5d567)をご確認ください。


<a id="org909b8ad"></a>

## 2.6. ボトムプレート取り付け

1.  ケースに `M3x4 なべねじ` でボトムプレートを取り付ける
2.  ボトムプレートの溝にゴム足を貼り付ける  
    ![img](./images/close_housing.jpg)


<a id="org6c9f4fb"></a>

## 2.7. キーキャップ取り付け

用意したお気に入りのキーキャップを取り付けてください。  
もう少しで完成です。


<a id="orgf2ca617"></a>

# 3. キーマップの設定

`Keymap` タブを表示し、お好みのキーマップを設定してください。

画面上部から変更したいキーをクリックし、その後、設定したいキーを画面下部から選択します。  
![img](./images/change_keymap.png)


<a id="orgd141837"></a>

# 4. メンテナンス


<a id="orgc81d1fb"></a>

## 4.1. ファームウェア更新

1.  ボトムプレートを取り外す
2.  USB Type-CケーブルでPCとYak40キーボードを接続する
3.  PCBの `BOOT` スイッチを押しながら `RESET` スイッチを押す  
    ![img](./images/reboot.jpg)
    -   PCにUSBストレージとして認識されます。
4.  認識したUSBストレージに新しいファームウェアをコピーする
    -   コピーが完了すると自動でUSBストレージが取り出され、キーボードとして認識されます。
5.  ボトムプレートを取り付ける


<a id="org4f5d567"></a>

# 5. トラブルシューティング


<a id="orge0104f9"></a>

## 5.1. キーボードがPCに認識されない

以下手順を順番に試してください。

1.  ドーターボードとPCBの接続を確認する
    -   ドーターボード・PCB両方のソケットの奥までコネクターが挿さっていることを確認してください。
2.  USB Type-Cケーブルが奥まで挿さっているか確認する
    -   コネクター部分の形状によってはケースと干渉する可能性があります。  
        別のUSB Type-Cケーブルでの接続もお試しください。
3.  [6. 連絡先](#org1574eca)に連絡する
    -   お手数をおかけしますが、連絡先のいずれかから私に連絡をしてください。  
        その際詳しい症状・写真も添付していただけますとありがたいです。


<a id="org6151273"></a>

## 5.2. 反応しないキーがある

以下手順を順番に試してください。

1.  反応しないキーのスイッチを外す
2.  キースイッチの足が曲がっていないことを確認する
    -   足が曲がっていた場合は新しいキースイッチに交換するか、足を真っ直ぐに修正してから再度取り付けてください。
3.  キースイッチが正しく挿さっていることを確認する
    -   キースイッチがスイッチプレートから浮いている場合は、浮かないように奥まで挿してください。
4.  [6. 連絡先](#org1574eca)に連絡する
    -   お手数をおかけしますが、連絡先のいずれかから私に連絡をしてください。  
        その際詳しい症状・写真も添付していただけますとありがたいです。


<a id="org6844cf7"></a>

## 5.3. ロータリーエンコーダーが反応しない

以下手順を順番に試してください。

1.  正しくはんだ付けできていることを確認する
    -   キーソケットとの共存のため、はんだ付け部分(パッド)が小さくなっています。  
        再度はんだごてでパッドを熱し、はんだ付けできていることを確認してください。
2.  [6. 連絡先](#org1574eca)に連絡する
    -   お手数をおかけしますが、連絡先のいずれかから私に連絡をしてください。  
        その際詳しい症状・写真も添付していただけますとありがたいです。


<a id="org1574eca"></a>

# 6. 連絡先

-   X(Twitter): [@kuriki<sub>sasa</sub>](https://x.com/kuriki_sasa)
-   Bluesky: [@kurikisasa.bsky.social](https://bsky.app/profile/kurikisasa.bsky.social)
-   Discord: kurikisasa
-   Discord server: <https://discord.gg/pC4t9NJStE>


<a id="org77cd219"></a>

# さいごに

無事、完成できましたでしょうか？

Yak40の設計データは全て[GitHub](https://github.com/kuriki-sasa/Yak40)で公開しています。  
自分で製造するもよし、参考にしてオリジナルを作るもよし、ライセンス範囲内でお好きにご活用ください。

良きキーボードライフを！

