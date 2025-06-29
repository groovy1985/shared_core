# ベースイメージ：Python3.10 + curl
FROM python:3.10

# 作業ディレクトリ作成
WORKDIR /app

# コードコピー
COPY . /app

# Pythonライブラリインストール
RUN pip install fastapi uvicorn pydantic

# APIサーバー起動時に使うポートを開放
EXPOSE 8000

# デフォルトはbashで起動
CMD [ "bash" ]
