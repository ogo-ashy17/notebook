# stlite-streamlit-app

このプロジェクトは、Streamlitを使用してインタラクティブなデータアプリケーションを作成するためのものです。stliteを利用して、StreamlitアプリをHTMLファイルから簡単に読み込むことができます。

## プロジェクト構成

- `src/streamlit_app.py`: Streamlitアプリケーションのエントリーポイントです。データの表示やインタラクティブな要素を作成します。
- `src/index.html`: stliteを使用してStreamlitアプリを読み込むためのHTMLファイルです。必要なスタイルシートやスクリプトを含み、`streamlit_app.py`を指定してアプリをマウントします。

## セットアップ手順

1. 必要なライブラリをインストールします。
   ```
   pip install streamlit pandas numpy openai==1.39.0
   ```

2. `src/index.html`をブラウザで開きます。これにより、Streamlitアプリが表示されます。

3. アプリケーションを実行するには、以下のコマンドを使用します。
   ```
   streamlit run src/streamlit_app.py
   ```

## 使用方法

アプリケーションを開いたら、データの表示やインタラクティブな要素を操作できます。アプリはリアルタイムでデータを更新し、ユーザーの入力に応じて反応します。

## ライセンス

このプロジェクトはMITライセンスの下で提供されています。