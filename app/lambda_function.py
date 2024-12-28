from modules import module_a
from repositories import sample_db


def lambda_handler(event, context):
    """
    サンプルLambdaハンドラ。
    module_aとsample_dbの両方を呼び出し、処理結果をまとめて返すだけ。
    """

    greeting = module_a.greet_user(event.get("name", "NoName"))
    db_response = sample_db.mock_db_access()

    print(
        {
            'StatusCode': 200,
            'Greeting': greeting,
            'DBResponse': db_response,
            'ReceivedEvent': event
        }
    )

    return {
        'StatusCode': 200,
        'Body': '正常に実行されました'
    }
