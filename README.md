# 多機能計算アプリ (CalcPro)

企業のインターンシップ応募のために作成した、PythonのGUIライブラリ`Flet`を使用したデスクトップアプリケーションです。

<img src="https://i.imgur.com/usN9bcd_d.webp?maxwidth=760&fidelity=grand" width="200">
<img src="https://i.imgur.com/YgW1IFE_d.webp?maxwidth=760&fidelity=grand" width="200">
<img src="https://i.imgur.com/QDbTMfg_d.webp?maxwidth=760&fidelity=grand" width="200">
<img src="https://i.imgur.com/0OSEVLD_d.webp?maxwidth=760&fidelity=grand" width="200">
<img src="https://i.imgur.com/7PDeq3U_d.webp?maxwidth=760&fidelity=grand" width="200">



## 概要

このアプリケーションは、日常的な計算から少し専門的な計算まで、一つのアプリで完結することを目指して開発しました。タブを切り替えることで、複数の機能を利用できます。

## 主な機能

- **標準電卓**:
  - 四則演算が可能なシンプルな電卓です。
- **日付計算**:
  - 現在時刻（和暦・西暦）をリアルタイムで表示します。
  - 2つの日付の間の日数を計算したり、特定の日数（例: 1000日）が何年何週間になるかを変換したりできます。
- **基数変換**:
  - 2進数、8進数、10進数、16進数をリアルタイムで相互変換します。
- **行列計算**:
  - 行列の数（最大10個）と各行列のサイズ（最大10x10）を変更して、積を計算できます。
- **比率計算**:
  - `A : B = C : D` のうち、一つの未知数を求める計算ができます。

## 技術スタック

- **言語**: Python 3
- **ライブラリ**:
  - Flet (GUIフレームワーク)
  - NumPy (行列計算)

## セットアップと実行方法

### 1. リポジトリのクローン

```bash
git clone https://github.com/Ncode320/CalcPro.git
cd CalcPro
```

### 2. 必要なライブラリのインストール

```bash
pip install -r requirements.txt
```

### 3. アプリケーションの実行

```bash
python main.py
```