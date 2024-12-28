FROM public.ecr.aws/lambda/python:3.12

# 依存パッケージのインストール
COPY requirements.txt .
RUN python3.12 -m pip install -r requirements.txt

# ソースコードをコンテナにコピー
COPY app ./

# Lambdaハンドラの指定
CMD ["lambda_function.lambda_handler"]
