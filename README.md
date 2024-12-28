# Docker Lambda Sample

このリポジトリは、Lambda を Docker でローカル実行するサンプルです。

## ディレクトリ構成

```
.
├── Dockerfile
├── Dockerfile.dev
├── README.md
├── app
│   ├── __init__.py
│   ├── entrypoint.py
│   ├── lambda_function.py
│   ├── modules
│   │   ├── __init__.py
│   │   └── module_a.py
│   └── repositories
│       ├── __init__.py
│       └── sample_db.py
└── requirements.txt
```

## ファイル説明

- **Dockerfile**: 本番用の Docker イメージを構築するための設定ファイル。
- **Dockerfile.dev**: 開発用の Docker イメージを構築するための設定ファイル。`entrypoint.py` を使ってローカル実行が可能。
- **app/**: アプリケーションのメインディレクトリ。
  - **entrypoint.py**: ローカル実行時にエントリーポイントとして動作するスクリプト。
  - **lambda_function.py**: Lambda のハンドラ関数。
  - **modules/**: アプリケーション内のユーティリティ関数やモジュール。
  - **repositories/**: データベースなど外部リソースとのやりとりを模擬するコード。

## ローカル環境

### ■ 環境

- Docker

### ■ 実行方法

1. **環境変数の設定**<br>
   [`.env.sample`](./.env.sample)を元に`.env`をプロジェクトのルートディレクトリに作成する。

2. **Docker イメージのビルド**<br>

   ```bash
   $ docker build -t docker-lambda-dev -f Dockerfile.dev .
   ```

   403 エラーが出る場合は認証を得る

   ```bash
   $ aws ecr-public get-login-password --region us-east-1 | docker login --username AWS --password-stdin public.ecr.aws
   ```

3. コンテナを実行

   JSON を渡して Lambda ハンドラをローカルで呼び出す:

   ```bash
   $ docker run --rm docker-lambda-dev '{"name":"Alice"}'
   ```

   引数がない場合:

   ```bash
   $ docker run --rm docker-lambda-dev
   ```

## 本番環境

### ■ 環境

- Lambda
- ECR

### ■ デプロイ方法

1. ECR<br>
   `［プッシュコマンドの表示］`から手順通りに ECR にイメージをプッシュ
2. Lambda<br>
   `［新しいイメージをデプロイ］`で ECR にプッシュした最新のイメージを選択する

### ■ テスト方法

- Lambda のテストイベントから下記の形式で実行可能
  ```bash
  {
    "name":"Alice"
  }
  ```
