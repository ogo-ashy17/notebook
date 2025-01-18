import os
import pandas as pd
import mlflow

from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report

# credential = DefaultAzureCredential()

# blob_service_client = BlobServiceClient(
#     'https://wsazureml2433882611.blob.core.windows.net',
#     credential
#     )

# container_client = blob_service_client.get_container_client('azureml-blobstore-408c658f-c52a-4e18-92ad-380bdc5430b6')

mlflow.set_experiment('test-experiment')
mlflow.sklearn.autolog()
with mlflow.start_run() as run:
    # データ読み込み
    df = pd.read_csv('./iris/iris.csv', encoding='utf-8')
    # 目的変数を数値に変換
    df.loc[df['target']=='setosa', 'target'] = '0'
    df.loc[df['target']=='versicolor', 'target'] = '1'
    df.loc[df['target']=='virginica', 'target'] = '2'

    # 学習・テストに分割
    X_train, X_test, y_train, y_test = train_test_split(df.drop('target', axis=1), df['target'], random_state=42)

    # ランダムフォレスト
    clf = RandomForestClassifier(random_state=42)
    clf.fit(X_train, y_train)

    pred = clf.predict(X_test)

    with open('result.txt', mode='w', encoding='utf-8') as f:
        f.write('confusion matrix:\n')
        f.write(str(confusion_matrix(y_test, pred)) + '\n')
        f.write('')
        f.write('classification report:\n')
        f.write(classification_report(y_test, pred, target_names=['0', '1', '2']))

    mlflow.log_artifact('./result.txt')